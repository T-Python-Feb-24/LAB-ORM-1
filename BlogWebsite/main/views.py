from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def home_page(request: HttpRequest):
    
    posts = Post.objects.all()

    return render(request,'main/home_page.html',{"posts":posts})


def add_post(request : HttpRequest):
    
    if request.method == "POST":
        new_post = Post(
            title = request.POST.get("title"),
            content = request.POST.get("content"),
            is_published = request.POST.get('is_published',False),
            poster = request.FILES["poster"]
            )
        
        new_post.save()
        return redirect("main:home_page")
     
    return render(request,"main/add_post.html")


def post_detail(request : HttpRequest ,post_id):
    
    post = Post.objects.get(pk=post_id)
     
    return render (request,"main/post_detail.html",{"post":post})


def delete_post(request : HttpRequest ,post_id):
    
    post = Post.objects.get(pk=post_id)
    post.delete()
    
    return redirect("main:home_page")


def update_post(request : HttpRequest ,post_id):
    
    post = Post.objects.get(pk=post_id)
    
    if request.method == "POST":
        
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.poster = request.FILES["poster"]
        post.is_published = request.POST.get("is_published", False)
        post.save()
        
        return redirect("main:post_detail", post_id = post.id)
    
    return render(request,"main/update_post.html",{"post":post})
