from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    file = CloudinaryField('video')  # Store songs in Cloudinary
    image = CloudinaryField('image', default="https://res.cloudinary.com/YOUR_CLOUD_NAME/image/upload/v1700000000/default.jpg")  # Default Cloudinary image
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title








