from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post


def home_view(request: HttpRequest):

    #get all entries insisde database
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }

    return render(request, "main/home.html", context)



def add_blog_view(request: HttpRequest):

    
    #adding a new entry
    if request.method == "POST":
        new_blog = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], published_at=request.POST["published_at"] )
        new_blog.save()
        return redirect("main:home_view")

    return render(request, "main/add.html")