from django.shortcuts import render, redirect
from django.utils import timezone  
from .models import Post

def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/index.html', {'posts': posts})

def add_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        is_published = 'is_published' in request.POST
        if is_published:
            published_at = timezone.now()
        else:
            published_at = None
        post = Post.objects.create(title=title, content=content, is_published=is_published, published_at=published_at)
        return redirect('index')
    return render(request, 'blog/add_blog.html')
