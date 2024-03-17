from django.db import models
from django.utils.text import TextChoices

# Create your models here.


class Post(models.Model):
    
    title = models.CharField(max_length=512)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField()



class CategoryChoices(TextChoices):
    General = 'General', 'General'
    Scince = 'Science', 'Science'
    Culture = 'Culture', 'Culture'
    Food = 'Food', 'Food'
    Tech = 'Tech', 'Tech'
    Fathion = 'Fashion', 'Fashion'



class Post(models.Model):
    # Existing fields in your post model

    category = models.CharField(
        max_length=10,
        choices=CategoryChoices.choices,
        default=CategoryChoices.General
    )

image = models.ImageField(upload_to="movies/images")