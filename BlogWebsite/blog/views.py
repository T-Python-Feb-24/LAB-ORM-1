from django.shortcuts import render, redirect,get_object_or_404
from .models import Post
from django.http import HttpRequest, HttpResponse
from django.utils import timezone  
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')

    try:
        paginated_posts = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)

    context = {
        'posts': paginated_posts,
    }
    return render(request, 'blog/home.html', context)


def add_post(request):
    try:
        CATEGORY_CHOICES = Post.CATEGORY_CHOICES
    except AttributeError:
        CATEGORY_CHOICES = []

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        is_published_str = request.POST.get('is_published')
        poster = request.FILES.get('poster')  
        is_published = is_published_str.lower() == 'true'
        
        post = Post.objects.create(
            title=title,
            content=content,
            category=category,
            is_published=is_published,
            poster=poster,  
            published_at=timezone.now()
        )
        
        return redirect('home')
    
    return render(request, 'blog/add_post.html', {'CATEGORY_CHOICES': CATEGORY_CHOICES})

#################################################################
def post_detail(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    return render(request, 'blog/post_detail.html', {'post': post})

def post_update(request: HttpRequest, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        try:
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.category = request.POST.get('category')
            post.is_published = request.POST.get('is_published') == 'on'  
            new_poster = request.FILES.get('poster')  
            
            if new_poster:
                post.poster = new_poster
            
            post.save()
            return redirect('post_detail', pk=post.pk)
        except Exception as e:
            print(e)

    return render(request, 'blog/update_post.html', {'post': post})

    
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog/post_delete_confirm.html', {'post': post})

def all_posts(request):
    search_query = request.GET.get('q', '')

    if search_query:
        posts = Post.objects.filter(
            is_published=True,
            title__icontains=search_query  
        ).order_by('-published_at')
    else:
        posts = Post.objects.filter(is_published=True).order_by('-published_at')

    category_counts = Post.objects.filter(is_published=True).values('category').annotate(count=Count('category'))

    context = {
        'posts': posts,
        'category_counts': category_counts,
        'search_query': search_query,  
    }
    return render(request, 'blog/all_posts.html', context)