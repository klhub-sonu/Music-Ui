from django.contrib import admin
from .models import Song, Category

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'category')  # Show these fields in the admin panel
    list_filter = ('category', 'artist')  # Filter options in the admin panel
    search_fields = ('title', 'artist')  # Add search functionality

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Show category names

# Register models with their admin configurations
admin.site.register(Song, SongAdmin)
admin.site.register(Category, CategoryAdmin)



