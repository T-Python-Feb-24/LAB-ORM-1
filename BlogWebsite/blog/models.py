from django.db import models

# Create your models here.

class Post(models.Model):

    #categories choices
    categories = models.TextChoices("Category", ["General", "Food", "Tech"])

    title = models.CharField(max_length=2024) #required
    content = models.TextField()
    is_published = models.BooleanField()
    published_at =  models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(max_length = 64, choices=categories.choices)

    