from django.urls import path
from django.shortcuts import render
from .views import index, register_view, login_view, logout_view
from .views import all_songs, edit_song
from .views import delete_song

# Home Page View
def index_view(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', index, name='index'),  # Music Player UI
    path('register/', register_view, name='register'),  # Registration
    path('login/', login_view, name='login'),  #  Login
    path('logout/', logout_view, name='logout'),  # User Logout
    path('', index_view, name='home'),  # Redirects to index.html
    path('all-songs/', all_songs, name='all_songs'),
    path("edit_song/<int:song_id>/", edit_song, name="edit_song"),
    path('delete_song/<int:song_id>/', delete_song, name='delete_song'),
]
