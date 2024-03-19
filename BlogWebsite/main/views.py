from django import forms
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Post
from datetime import datetime
from django.db.models import Q
from django.utils.timezone import now

def home(request: HttpRequest):
    posts = Post.objects.all()
    print(request.GET)
    posts = Post.objects.all().order_by('-published_at')[0:3]
    

    return render(request, "main/home.html", {"posts" : posts})

def all_posts_view(request: HttpRequest):

    
    if "cat" in request.GET:
        posts = Post.objects.filter(category=request.GET["cat"])
    else:
        posts = Post.objects.all()

    return render(request, "main/all_posts.html", {"posts" : posts, "categories" : Post.categories.choices})


def add_post(request: HttpRequest):

    if request.method == 'POST':
        try:
            new_post = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST.get("is_published", False), category=request.POST["category"], image=request.FILES["image"])
            new_post.save()
        except Exception as e:
            print(e)
        return redirect("main:home")
    return render(request, "main/add_post.html", {"categories" : Post.categories.choices})



def post_detail(request:HttpRequest, post_id):

    try:
        #getting a  post detail
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
         return render(request, "404.html")
    except Exception as e:
        print(e)

    return render(request, "main/post_detail.html", {"post" : post})

def update_post(request:HttpRequest, post_id):

    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        try:
            
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST.get("is_published", False)
            post.category = request.POST["category"]
            post.image = request.FILES.get("image", post.image)
            post.save()
            return redirect("main:post_detail", post_id=post.id)
        except Exception as e:
            print(e)

    
    return render(request, 'main/update_post.html', {"post" : post, "categories" : Post.categories.choices})


def delete_post(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)

    return redirect("main:home")


def view_404(request, exception):
    return render(request, '404.html')

def search_posts(request):
    query = request.GET.get('q', '')  # Get the title query, default to empty string if not provided
    publish_date_str = request.GET.get('publish_date', '')  # Get the publish date string from the form

    search_results = Post.objects.all()

    
    if query:
        search_results = search_results.filter(title__icontains=query)

   
    if publish_date_str:
        try:
            publish_date = datetime.strptime(publish_date_str, '%Y-%m-%d').date()
            search_results = search_results.filter(published_at__date=publish_date)
        except ValueError:
            
            pass

    return render(request, 'main/search.html', {
        'search_results': search_results,
        'query': query,
    })