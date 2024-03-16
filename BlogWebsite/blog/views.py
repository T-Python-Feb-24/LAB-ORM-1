from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post


def home_page(request:HttpRequest):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, 'blog/home_page.html', context)

def add_post_page(request: HttpRequest):
    
    if request.method =="POST":
        new_post = Post(
            title = request.POST["title"], 
            content = request.POST["content"],  
            published_at = request.POST["published_at"], 
            is_published = request.POST.get("is_published")
        )
        new_post.save()
        return redirect("blog:home_page")
    
    return render(request, "blog/add_post_page.html")