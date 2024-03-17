from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import BlogWebsite


def index(request: HttpRequest):

    
    blog = BlogWebsite.objects.all()
    context = {
        "blog" : blog
    }

    return render(request, "Website/index.html", context)



def add_post(request: HttpRequest):

    
    
    if request.method == "POST":
        new_post = BlogWebsite(title=request.POST["title"], content=request.POST["content"],is_published =request.POST["published_at"], published_at=request.POST["published_at"])
        new_post.save()
        return redirect("Website:index")
    return render(request, "Website/add_post.html")