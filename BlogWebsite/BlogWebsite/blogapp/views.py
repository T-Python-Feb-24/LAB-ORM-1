from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.utils import timezone

def index_view(request):
    posts = Post.objects.filter(is_published=True)

    return render(request, 'blogapp/index.html', {'posts': posts})

def add_post_view(request: HttpRequest):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        if not title or not content:
            # Handle the error and render the form again with an error message
            return render(request, "blogapp/add_post.html", {"error": "Title and content are required."})

        new_note = Post(title=title, content=content, is_published=True)
        new_note.published_date = timezone.now()
        new_note.save()
        return redirect("main:index")

    return render(request, "blogapp/add_post.html")