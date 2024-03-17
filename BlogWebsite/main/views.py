from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Post
from datetime import date

# Create your views here.


def post_view(request: HttpRequest):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "main/index.html", context)


def add_post_view(request: HttpRequest):
    try:
        if request.method == "POST":
            new_post = Post(
                title=request.POST.get("title"),
                content=request.POST.get("content"),
                is_published=request.POST.get("is_published", False),
                poster=request.FILES.get("poster"))
            new_post.save()
            return redirect("main:post_view")

    except Exception as e:
        print(e)
    return render(request, "main/add_post.html")


def post_detail_view(request: HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, "404.html")
    except Exception as e:
        print(e)

    return render(request, "main/post_detail.html", {"post": post})


def update_post_view(request: HttpRequest, post_id):

    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        try:
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST.get("is_published", False)
            post.save()
            return redirect("main:post_detail_view", post_id=post.id)
        except Exception as e:
            print(e)

    return render(request, 'main/update_post.html', {"post": post})


def delete_post_view(request: HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)

    return redirect("main:post_view")
