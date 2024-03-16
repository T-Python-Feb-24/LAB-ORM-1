from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=2024)
    content = models.TextField()
    published_at =  models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(blank=True, null=True)

    