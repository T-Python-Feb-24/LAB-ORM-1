from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post


def index_view(request: HttpRequest):

    #get all entries insisde database
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }

    return render(request, "main/index.html", context)



def add_content_view(request: HttpRequest):

    
    #adding a new entry
    if request.method == "POST":
        new_note = Post(title=request.POST["title"], content=request.POST["content"])
        new_note.save()
        return redirect("main:index_view")

    return render(request, "main/update-post.html")