from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  
from .forms import RegisterForm
from .models import Song, Category
import json
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .forms import SongUploadForm


def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    
    if request.method == "POST":
        song.delete()
        return redirect('/')  # Redirect to home after deleting
    
    return render(request, 'confirm_delete.html', {'song': song})


# Function to check if the user is an admin
def is_admin(user):
    return user.is_staff  # Only allows admin users

@user_passes_test(is_admin)  # Only admins can access this page
def all_songs(request):
    songs = Song.objects.all()  # Fetch all songs
    categories = Category.objects.all()

    if request.method == "POST":
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save song to database
            return redirect("all_songs")  # Refresh the page after upload
    else:
        form = SongUploadForm()

    return render(request, "all_songs.html", {"songs": songs, "categories": categories, "form": form})

@user_passes_test(is_admin)  # Only admins can access
def edit_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    
    if request.method == "POST":
        form = SongUploadForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect("all_songs")  # Redirect back to all songs list
    else:
        form = SongUploadForm(instance=song)

    return render(request, "edit_song.html", {"form": form, "song": song})




# Function to check if user is an admin or a registered user
@login_required
def all_songs(request):
    songs = Song.objects.all()  # Fetch all songs
    categories = Category.objects.all()
    
    user = request.user  # Get the logged-in user
    welcome_message = f"Welcome, {user.username}!"  # Welcome message with username

    if request.method == "POST":
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save song to database
            return redirect("all_songs")  # Refresh the page after upload
    else:
        form = SongUploadForm()

    return render(
        request, 
        "all_songs.html", 
        {
            "songs": songs, 
            "categories": categories, 
            "form": form, 
            "welcome_message": welcome_message
        }
    )




def index(request):
    categories = Category.objects.all()  # Fetch all categories
    selected_category = request.GET.get("category", "")
    search_query = request.GET.get("q", "")  # Get search input

    # Fetch songs based on category selection and search query
    songs = Song.objects.all()

    if request.user.is_authenticated:
        if selected_category:
            songs = songs.filter(category__name__iexact=selected_category)

        if search_query:
            songs = songs.filter(
                title__icontains=search_query
            ) | songs.filter(
                artist__icontains=search_query
            ) | songs.filter(
                category__name__icontains=search_query
            )

    tracks_json = json.dumps([
        {
            "title": song.title,
            "artist": song.artist,
            "category": song.category.name if song.category else "",
            "image": song.image.url if song.image else "",
            "file": song.file.url if song.file else ""
        } 
        for song in songs
    ])

    return render(request, "index.html", {
        "tracks_json": tracks_json,
        "categories": categories,
        "selected_category": selected_category,
        "search_query": search_query,  # Pass search query to template
    })




def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "You have successfully registered. Please log in.")  
            return redirect('login')  # Redirect to login page
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged into Music Player App..!") 
            return redirect('/')  # Redirect to the homepage (index.html)
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")  
    return redirect('login')  # Redirect to login after logout , models.py : from django.db import models

