from django.db import models


class Post(models.Model):
    
    categories = models.TextChoices("Category", ["General", "Tech", "Science", "Sports", "Economy"])
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/4614.jpeg.webp')
    category = models.CharField(max_length=30, choices=categories.choices)

    
