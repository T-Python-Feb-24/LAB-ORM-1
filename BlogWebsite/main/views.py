from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Post
from .forms import PostForm
# Create your views here.

def home_page(request:HttpRequest):

    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request,'main/home.html', context)

def add_post_page(request:HttpRequest):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home_page')
    else:
        form = PostForm()
    return render(request, 'main/add_post.html', {'form': form})