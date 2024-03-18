from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/default_img.jpg')
    
    # class Category(models.TextChoices):
    #     GENERAL = 'General'
    #     SCIENCE = 'Science'
    #     CULTURE = 'Culture'
    #     FOOD = 'Food'
    #     TECH = 'Tech'
    #     FASHION = 'Fashion'

    Categories = models.TextChoices('Category', ["General","Science", "Culture", "Food","Tech","Fashion"]) 
    category = models.CharField(max_length = 64, choices = Categories.choices)