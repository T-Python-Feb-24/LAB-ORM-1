from django.db import models

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField()