from django.db import models
from django.utils import timezone

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('General', 'General'),
        ('Science', 'Science'),
        ('Culture', 'Culture'),
        ('Food', 'Food'),
        ('Tech', 'Tech'),
        ('Fashion', 'Fashion'),
    ]
     
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(default=timezone.now)
    poster = models.CharField(max_length=100)  # Assuming a CharField for the poster's name
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)


    def __str__(self):
        return self.title
