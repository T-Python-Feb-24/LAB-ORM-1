from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.


def post_view(request: HttpRequest):
    post = Post.objects.all()
    context = {
        "posts": post
    }
    return render(request, "main/index.html", context)


def add_post_view(request: HttpRequest):
    if request.method == "POST":
        if "is_published" in request.POST:
            new_post = Post(
                title=request.POST["title"], content=request.POST["content"],
                is_published=request.POST["is_published"],
                published_at=request.POST["published_at"])
            new_post.save()
        else:
            new_post = Post(
                title=request.POST["title"], content=request.POST["content"])
            new_post.save()
            return redirect("main:post_view")
    return render(request, "main/add_post.html")
