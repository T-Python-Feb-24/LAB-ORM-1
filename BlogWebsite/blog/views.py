from datetime import date, timedelta
import os
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post


def home_page(request:HttpRequest):
      #getting the Query Parameters
    print(request.GET)

    #limiting the result using slicing
    posts = Post.objects.all().order_by('-published_at')[0:3]

    return render(request, "blog/home_page.html", {"posts" : posts})


def add_post_page(request: HttpRequest):
    if request.method =="POST":
        try:
            new_post = Post(
                title = request.POST["title"], 
                content = request.POST["content"],  
                is_published = request.POST.get("is_published", False),
                category = request.POST["category"],
                poster = request.FILES.get("poster", Post.poster.field.default)
            )

            new_post.save()

        except Exception as e:
            print(e)
        return redirect("blog:home_page")
    
    return render(request, "blog/add_post_page.html",{"categories" : Post.categories.choices})


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
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST.get("is_published", False)
            post.poster = request.FILES.get("poster", post.poster)
            post.category = request.POST["category"]
            post.save()

            return redirect("blog:post_detail_page", post_id=post.id)
        except Exception as e:
            print(e)

    
    return render(request, 'blog/update_post_page.html', {"post" : post , "categories" : Post.categories.choices})

def delete_post_page(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("blog:home_page")


def all_posts_page(request: HttpRequest):

    
    if "cat" in request.GET:
        posts = Post.objects.filter(category=request.GET["cat"])
    else:
        posts = Post.objects.all()

    return render(request, "blog/all_posts_page.html", {"posts" : posts, "categories" : Post.categories.choices})

def posts_search_page(request: HttpRequest):

    posts = []

    if "search" in request.GET:
        posts = Post.objects.filter(title__contains=request.GET["search"])

    if "date" in request.GET and len(request.GET["date"]) > 4:
        first_date = date.fromisoformat(request.GET["date"])
        end_date = first_date + timedelta(days=1)
        posts = posts.filter(published_at__gte=first_date, published_at__lt=end_date)


    return render(request, "blog/posts_search_page.html", {"posts" : posts})

