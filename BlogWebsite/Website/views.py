from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse ,Http404
from .models import BlogWebsite


def index(request: HttpRequest):

    
    blog = BlogWebsite.objects.all()
    context = {
        "blog" : blog
    }

    return render(request, "Website/index.html", context)



def add_post(request: HttpRequest):

    
    
    if request.method == "POST":
        new_post = BlogWebsite(title=request.POST["title"], content=request.POST["content"],is_published =request.POST["published_at"], published_at=request.POST["published_at"])
        new_post.save()
        return redirect("Website:index")
    return render(request, "Website/add_post.html")


def post_detail(reqest:HttpRequest,post_id):
    
    post= BlogWebsite.objects.get(pk=post_id)
    
    return render(reqest, "Website/post_detail.html",{"post": post})


def update_post(request:HttpRequest, post_id):
    post=BlogWebsite.objects.get(pk=post_id)
    if request.method == "POST":
        try:
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST.get("is_published", False)
            post.save()
            return redirect("Website/post_detail.html", post_id=post.id)
        except Exception as e:
            print(e)
    return render(request,'Website/post_detail.html',{"post":post})


def delete_post(request:HttpRequest, post_id):

    try:
        post =BlogWebsite.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("Website:index")

def view_404(request, exception):
    return render(request, '404.html')
