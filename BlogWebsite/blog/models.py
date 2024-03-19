# models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('General', 'General'),
        ('Science', 'Science'),
        ('Culture', 'Culture'),
        ('Food', 'Food'),
        ('Tech', 'Tech'),
        ('Fashion', 'Fashion'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(default=timezone.now)
    poster = models.ImageField(upload_to="images/", default="images/regular.jpg")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
