from django.db import models

class Category(models.TextChoices):
    GENERAL = 'General', 'General'
    SCIENCE = 'Science', 'Science'
    CULTURE = 'Culture', 'Culture'
    FOOD = 'Food', 'Food'
    TECH = 'Tech', 'Tech'
    FASHION = 'Fashion', 'Fashion'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/default.webp')
    category_choices = models.CharField(max_length=20, choices=Category.choices, default=Category.GENERAL)

    def __str__(self):
        return self.title
