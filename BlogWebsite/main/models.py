from django.db import models

# Create your models here.
class Post(models.Model):
   
    categories=models.TextChoices("Category",["General","Tech","Science","Fashoin","Food","Culture"])


    title = models.CharField(max_length=2024)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="images/default.jpeg")
    category=models.CharField(max_length=64 ,choices=categories.choices)

    #عشان اغير الطريقة الي تظهر في الامن جانقو
    def __str__(self) :
        return self.title
       
    