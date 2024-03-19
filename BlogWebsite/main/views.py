from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.

def index_view(request:HttpRequest):

    #getting the Query Parameters
    print(request.GET)

    #limiting the result using slicing
    posts = Post.objects.filter(is_published=True).order_by('-published_at')[:3]


    return render(request, "main/index.html", {"posts" : posts})


def all_posts_view(request: HttpRequest):
    selected_category = request.GET.get("cat")
    posts = Post.objects.filter(category=selected_category) if selected_category else Post.objects.all()
    categories = Post.categories.choices

    return render(request, "main/all_posts.html", {"posts": posts, "selected_category": selected_category, "categories": categories})

def search_view(request):
    query = request.GET.get('q')
    publish_date = request.GET.get('publish_date')

    posts = Post.objects.all()

    if query:
        posts = posts.filter(title__icontains=query)

    if publish_date:
        posts = posts.filter(published_at__date=publish_date)

    return render(request, 'main/search.html', {'posts': posts})

def add_post_view(request: HttpRequest):
 
    if request.method == 'POST':
        try:
            new_post = Post(
                title=request.POST["title"], 
                content=request.POST["content"], 
                is_published=request.POST.get("is_published", False), 
                category= request.POST["category"],  
                poster=request.FILES["poster"]
                )
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
            post.category = request.POST["category"]
            post.is_published = request.POST.get("is_published", False)
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

        