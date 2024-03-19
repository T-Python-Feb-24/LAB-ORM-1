from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post


def index_view(request: HttpRequest):

    posts = Post.objects.all()

    return render(request, "main/index.html", {"posts" : posts})


def add_post_view(request: HttpRequest):

    if request.method == 'POST':
        try:
            new_post = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST.get("is_published", False), poster=request.FILES["poster"])
            new_post.save()
            return redirect("main:index_view")
        except Exception as e:
            print(e)
    return render(request,"main/add_post.html")



def post_detail_view(request:HttpRequest, post_id):

    try:

        #getting a  post detail
         post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        post = None
    except Exception as e:
        print(e)

    return render(request, "main/post_detail.html", {"post" : post})


def update_post_view(request:HttpRequest, post_id):

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

    
    return render(request, 'main/update_post.html', {"post" : post})


def delete_post_view(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("main:index_view")


def search_post_view(request: HttpRequest):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Post.objects.filter(title__icontains=q)
    else:
        posts = Post.objects.all().order_by('-published_at')
        
    
    return render(request,"main/search_result.html",{"posts":posts})


