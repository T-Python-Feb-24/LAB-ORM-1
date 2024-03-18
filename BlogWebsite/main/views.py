from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def home_page(request: HttpRequest):
    
    posts = Post.objects.all()

    return render(request,'main/home_page.html',{"posts":posts})


def add_post(request : HttpRequest):
    
    if request.method == "POST":
        try:
            new_post = Post(
                title = request.POST.get("title"),
                content = request.POST.get("content"),
                is_published = request.POST.get('is_published',False),
                poster = request.FILES["poster"],
                category = request.P["category"]
                )
            new_post.save()
            return redirect("main:home_page")
        except Exception as e : 
            print(e)
            
    return render(request,"main/add_post.html",{"categories":Post.categories.choices})


def post_detail(request : HttpRequest ,post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
         return render(request,"main/not_found.html")
    except Exception as e:
        print(e)
    return render (request,"main/post_detail.html",{"post":post})


def delete_post(request : HttpRequest ,post_id):
    
    post = Post.objects.get(pk=post_id)
    post.delete()
    
    return redirect("main:home_page")


def update_post(request : HttpRequest,post_id):
    
    post = Post.objects.get(pk=post_id)
    
    if request.method == "POST":
        
        try:
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST.get("is_published", False)
            post.poster = request.FILES.get("poster", post.poster)
            post.save()
            return redirect("main:post_detail", post_id = post.id)
        except Exception as e :
           print(e)
       
    return render(request,"main/update_post.html",{"post":post})

