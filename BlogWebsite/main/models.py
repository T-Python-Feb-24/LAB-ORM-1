from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Post(models.Model):

    categories = models.TextChoices("Category", ["General",  "Science", "Culture", "Food", "Tech", "Fashion"])
    
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="images/def.jpg")
    category = models.CharField(max_length=30, choices=categories.choices)