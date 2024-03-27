from django.db import models

# Create your models here.

class Post(models.Model):

    categories = models.TextChoices("Category", ["General", "Tech", "Science", "Fashion"])

    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="images/default.jpeg")


