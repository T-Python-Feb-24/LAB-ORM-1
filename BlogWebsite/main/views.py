from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post


def home_view(request: HttpRequest):

    #get all entries insisde database
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }

    return render(request, "main/home.html", context)



def add_blog_view(request: HttpRequest):

    
    #adding a new entry
    if request.method == "POST":
        new_blog = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST.get("is_published", False), poster=request.FILES["poster"])
        new_blog.save()
        return redirect("main:home_view")

    return render(request, "main/add.html")

def detail_view(request:HttpRequest, post_id):

    try:
        #getting a  post detail
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return redirect("main:not_found_view")
        post = None
    except Exception as e:
        print(e)


    return render(request, "main/detail.html", {"post" : post})

def update_view(request:HttpRequest, post_id):

    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        try:
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST.get("is_published", False)
            post.poster=request.FILES["poster"]
            post.save()
            return redirect("main:detail_view", post_id=post.id)
        except Exception as e:
            print(e)

    
    return render(request, 'main/update.html', {"post" : post})


def delete_view(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("main:home_view")

def not_found_view(request:HttpRequest):
    return render(request,'main/404.html')
