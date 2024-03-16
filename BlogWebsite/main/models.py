from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
