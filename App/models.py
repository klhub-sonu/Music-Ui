from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    file = models.FileField(upload_to="songs/")
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title







