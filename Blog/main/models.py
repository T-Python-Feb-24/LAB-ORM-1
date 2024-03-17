from django.db import models

# Create your models here.
class Post(models.Model):

    class Category(models.TextChoices):
        GENERAL = 'General', 'General'
        SCIENCE = 'Science', 'Science'
        CULTURE = 'Culture', 'Culture'
        FOOD = 'Food', 'Food'
        TECH = 'Tech', 'Tech'
        FASHION = 'Fashion', 'Fashion'

    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="images/default.jpeg")
    category = models.CharField(max_length=20,choices=Category.choices,default=Category.GENERAL)

