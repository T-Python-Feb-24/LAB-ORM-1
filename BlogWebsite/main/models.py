from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=512)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)