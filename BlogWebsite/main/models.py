from django.db import models

# Create your models here.


class Post(models.Model):

    class category_choices(models.TextChoices):
        General = "General"
        Science = "Science"
        Culture = "Culture"
        Food = "Food"
        Tech = "Tech"
        Fashion = "Fashion"

    title = models.CharField(max_length=2048)
    category = models.CharField(max_length=7,
                                choices=category_choices.choices,
                                default=category_choices.General)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(
        upload_to="images/", default="images/default.jpeg")
