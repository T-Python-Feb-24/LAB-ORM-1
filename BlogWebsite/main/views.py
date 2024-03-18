from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post#, MyChoices
# Create your views here.

def index_view(request:HttpRequest):

    #get all entries insisde database
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }

    return render(request, "main/index.html", context)


def add_post_view(request: HttpRequest):
    #categories = MyChoices.choices ---  there is an error here i dont know how to solve it
 
    if request.method == 'POST':
        try:
            new_post = Post(
                title=request.POST["title"], 
                content=request.POST["content"],
                # category=request.POST["category"], 
                is_published=request.POST.get("is_published", False), 
                poster=request.FILES["poster"]
            )
            new_post.save()
            return redirect("main:index_view")
        except Exception as e:
            print(e)

    return render(request, "main/add_post.html")


def post_detail_view(request:HttpRequest, post_id):

    try:
        #getting a  post detail
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, 'main/not_exist.html')
    except Exception as e:
        print(e)
    return render(request, "main/post_detail.html", {"post" : post})

def update_post_view(request:HttpRequest, post_id):

    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        try:
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            # post.category = request.POST["category"]
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

        