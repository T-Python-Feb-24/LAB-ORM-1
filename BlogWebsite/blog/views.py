from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpRequest, HttpResponse
from django.utils import timezone  
from .forms import PostForm  

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html',context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})