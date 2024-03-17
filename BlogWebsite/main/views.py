from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.

def home_page(request: HttpRequest):
    context ={}
    
    posts = Post.objects.all()
    context={
        "posts":posts
    }
    
    return render(request,'main/home_page.html',context)


def add_post(request : HttpRequest):
    
    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"],published_at=request.POST["published_at"])
        new_post.save()
        return redirect("main:home_page")
     
    return render(request,"main/add_post.html")
