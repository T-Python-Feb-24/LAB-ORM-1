from django import forms
from .models import Post

class PostFrom(forms.ModelForm):
    class Mate:
        model=Post
        fields=['is_published' , 'published_at']