from django.db import models

# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=2024)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_at= models.DateTimeField()
    