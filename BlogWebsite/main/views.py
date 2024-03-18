from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Post
from django.db.models import Q
# Create your views here.

def home(request:HttpRequest):
    if "pub" in request.GET:
        posts = Post.objects.filter(is_published = request.GET.get("pub", default=True))[0:3]
    else:
        posts = Post.objects.all().filter(is_published = request.GET.get("pub", True))[0:3]

    return render(request, "main/home.html", {"posts" : posts})

def add_post(request:HttpRequest):

    if request.method == 'POST':
        try:
            new_post = Post(
                title = request.POST["title"], 
                content = request.POST["content"], 
                is_published = request.POST.get("is_published", False), 
                image = request.FILES.get("image", Post.image.field.default),
                category = request.POST['category']
            )
            new_post.save()
            
        except Exception as e:
            print(e)
        return redirect("main:home")
    
    
    return render(request, "main/add_post.html", {'category' : Post.Categories.choices})

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
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return render(request, "404.html")

        if request.method == "POST":
            try:
                post.title = request.POST["title"]
                post.content = request.POST["content"]
                post.is_published = request.POST.get("is_published", False)
                post.image = request.FILES.get('image', post.image)
                post.category = request.POST['category']
                post.save()
            except Post.DoesNotExist:
                return render(request, "404.html")
            except Exception as e:
                print(e)
            return redirect("main:post_detail", post_id= post.id)

        return render(request, 'main/update_post.html', {"post" : post, 'category' : Post.Categories.choices})


def delete_post(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, "404.html")
    
    try:
        post.delete()
    except Exception as e:
        print(e)
    
    return redirect("main:home")

def all_posts(request: HttpRequest):

    
    if "cat" in request.GET:
        posts = Post.objects.filter(category = request.GET["cat"])
    else:
        posts = Post.objects.all().order_by("-published_at") 

    return render(request, "main/all_post.html", {"posts" : posts, "category" : Post.Categories.choices})

def search(request: HttpRequest):
    if 'q' in request.GET:
        q = request.GET['q']
        # posts = Post.objects.filter(title__icontains=q)
        m_q = Q(Q(title__icontains=q) | Q(published_at__icontains=q) | Q(category__icontains=q))
        posts = Post.objects.filter(m_q)
    else:
        posts = Post.objects.all().order_by('-published_at')
    
    return render(request,"main/search_result.html",{"posts":posts})

# def view_404(request, exception):
#     return render(request, '404.html')