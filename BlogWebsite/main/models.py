from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=2024)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="images/default.jpeg")
    class Category(models.TextChoices):
        GENERAL='General'
        SCIENCE='Science'
        CULTURE='Culture'
        FOOD='Food'
        TECH='Tech'
        FASHON='Fashon'
   # category_choices= models.CharField(max_lenght=22 ,choices=Category, default= Category.GENERAL)
