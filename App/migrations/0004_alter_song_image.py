# Generated by Django 5.1.6 on 2025-02-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_category_name_alter_song_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
