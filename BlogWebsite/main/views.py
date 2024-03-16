from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Post
from datetime import date
def home(request: HttpRequest):
    
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'main/home.html', {'posts': posts})

def add_post(request: HttpRequest):
    
    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
            is_published=request.POST.get("is_published", "off") == "on"
        )
        new_post.save()
        return redirect('home')
    return render(request, 'main/add_post.html')
