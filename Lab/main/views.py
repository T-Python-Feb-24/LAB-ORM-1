from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import blog

def Blog (request: HttpRequest):

    #get all entries insisde database
    blogs = blog.objects.all()
    context = {
        "blogs" : blogs
    }
    return render(request,"main/home.html" , context)


def add_blog(request: HttpRequest):

    
    #adding a new entry
    if request.method == "POST":
        new_blog = blog(title=request.POST["title"], content=request.POST["content"] , is_published=request.POST["is_published"] ,  published_at=request.POST["published_at"])
        new_blog.save()
        return redirect("main:home")
        

    return render(request, "main/add_blog.html")