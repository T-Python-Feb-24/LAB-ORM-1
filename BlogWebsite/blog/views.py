import os
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post


def home_page(request:HttpRequest):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, "blog/home_page.html", context)


def add_post_page(request: HttpRequest):
    
    if request.method =="POST":
        try:
            new_post = Post(
                title = request.POST["title"], 
                content = request.POST["content"],  
                is_published = request.POST.get("is_published", False),
                poster=request.FILES["poster"]
            )
            new_post.save()
        except Exception as e:
            print(e)
        return redirect("blog:home_page")
    
    return render(request, "blog/add_post_page.html")


def post_detail_page(request:HttpRequest, post_id):
    
    try:
        #getting a  post detail
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, "blog/not_found_page.html")
    except Exception as e:
        print(e)

    return render(request, "blog/post_detail_page.html", {"post" : post})

def update_post_page(request:HttpRequest, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        try:
            if len(request.FILES) != 0:
                if len(post.poster) > 0:
                    os.remove(post.poster.path)
                post.poster = request.FILES["poster"]
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST.get("is_published", False)
            post.save()

            return redirect("blog:post_detail_page", post_id=post.id)
        except Exception as e:
            print(e)

    
    return render(request, 'blog/update_post_page.html', {"post" : post})

def delete_post_page(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("blog:home_page")
