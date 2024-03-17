from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
from django.utils import timezone
# Create your views here.

def index_view(request:HttpRequest):

    #get all entries insisde database
    blogs = Blog.objects.all()
    context = {
        "blogs" : blogs
    }

    return render(request, "main/index.html", context)

def add_blog_view(request:HttpRequest):

    #adding a new entry
    if request.method == "POST":
        # Get the value of is_published from the form
        is_published_value = request.POST.get("is_published")

        # Convert "on" to True, otherwise set it to False
        is_published = is_published_value == "on"
        
        new_blog = Blog(
            title=request.POST["title"], 
            content=request.POST["content"], 
            is_published=is_published, 
            published_at=request.POST.get("published_at") or timezone.now()
        )
        new_blog.save()
        return redirect("main:index_view")

    return render(request, "main/add_blog.html")