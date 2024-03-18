from django.db import models

# Create your models here.
class BlogWebsite(models.Model):
    
    title = models.CharField(max_length=2024)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="images/default.jpeg")

class Category(models.TextChoices):
    GENERAL = 'General'
    SCIENCE = 'Science'
    CULTURE = 'Culture'
    FOOD = 'Food'
    TECH = 'Tech'
    FASHION = 'Fashion'

    category_choices = models.CharField(max_length=10, choices=Category.choices, default=Category.GENERAL)
