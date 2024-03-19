from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post


def index_view(request: HttpRequest):

    #getting the Query Parameters
    print(request.GET)

    #limiting the result using slicing
    posts = Post.objects.all().order_by('-published_at')[0:3]


    return render(request, "main/index.html", {"posts" : posts})


def all_posts_view(request: HttpRequest):

    
    if "cat" in request.GET:
        posts = Post.objects.filter(category=request.GET["cat"])
    else:
        posts = Post.objects.all()

    return render(request, "main/all_posts.html", {"posts" : posts, "categories" : Post.categories.choices})

def add_post_view(request: HttpRequest):

    if request.method == 'POST':
        try:
            new_post = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST.get("is_published", False), category= request.POST["category"],  poster=request.FILES["poster"])
            new_post.save()
            return redirect("main:index_view")
        except Exception as e:
            print(e)

    return render(request, "main/add_post.html", {"categories" : Post.categories.choices})




def post_detail_view(request:HttpRequest, post_id):

    try:
        #getting a  post detail
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, "main/not_found.html")
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
            post.category = request.POST["category"]
            post.poster = request.FILES.get("poster", post.poster)
            post.save()
            return redirect("main:post_detail_view", post_id=post.id)
        except Exception as e:
            print(e)

    
    return render(request, 'main/update_post.html', {"post" : post, "categories" : Post.categories.choices})


def delete_post_view(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("main:index_view")

def search(request: HttpRequest):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Post.objects.filter(title__icontains=q)
    else:
        posts = Post.objects.all().order_by('-published_at')
    
    return render(request,"main/search_result.html",{"posts":posts})



