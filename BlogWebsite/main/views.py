from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Post

# Create your views here.

def home(request:HttpRequest):

    posts = Post.objects.all()

    return render(request, "main/home.html", {"posts" : posts})

def add_post(request:HttpRequest):

    if request.method == 'POST':
        try:
            new_post = Post(
                title=request.POST["title"], 
                content=request.POST["content"], 
                is_published=request.POST.get("is_published", False), 
                image=request.FILES["image"],
            )
            new_post.save()
            
        except Exception as e:
            print(e)
        return redirect("main:home")
    
    return render(request, "main/add_post.html")

def post_detail(request:HttpRequest, post_id):

    try:
        #getting a  post detail
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        post = None
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
            post.image = request.FILES['image']
            post.save()
        except Exception as e:
            print(e)
        return redirect("main:post_detail", post_id= post.id)

    return render(request, 'main/update_post.html', {"post" : post})


def delete_post(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    
    return redirect("main:home")


def view_404(request, exception):
    return render(request, '404.html')