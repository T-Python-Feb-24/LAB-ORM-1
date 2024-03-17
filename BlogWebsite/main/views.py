from django.shortcuts import render,redirect
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
        new_post = Post(title=request.POST.get("title"), content = request.POST.get("content"),is_published = request.POST.get('is_published'))
        new_post.save()
        return redirect("main:home_page")
     
    return render(request,"main/add_post.html")
