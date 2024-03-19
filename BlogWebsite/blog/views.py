from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post
from datetime import datetime



def index(request):
    # posts = Post.objects.all()

     #getting the Query Parameters
    print(request.GET)

    #limiting the result using slicing
    posts = Post.objects.all().order_by('-published_at')[0:3]
    return render(request, "blog/index.html", {"posts" : posts})
    


def all_posts_view(request: HttpRequest):

    
    if "cat" in request.GET:
        posts = Post.objects.filter(category=request.GET["cat"])
    else:
        posts = Post.objects.all()

    return render(request, "blog/all_posts.html", {"posts" : posts, "categories" : Post.categories.choices})

def add_blog(request: HttpRequest):

    if request.method == 'POST':
        try:
            new_post = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST.get("is_published", False), category= request.POST["category"],  poster=request.FILES["poster"])
            new_post.save()

        except Exception as e:
            print(e)
        return redirect("blog:index")
    
    return render(request, "blog/add_blog.html", {"categories" : Post.categories.choices})

def add_post_view(request: HttpRequest):

    if request.method == 'POST':
        try:
            new_post = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST.get("is_published", False), poster=request.FILES["poster"])
            new_post.save()
        except Exception as e:
            print(e)

    return render(request, "blog/add_blog.html")



def post_detail_view(request:HttpRequest, post_id):

    try:
        #getting a  post detail
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, "blog/not_found.html")
    except Exception as e:
        print(e)

    return render(request, "blog/post_detail.html", {"post" : post})


def update_post_view(request:HttpRequest, post_id):

    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        try:
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST.get("is_published", False)
            post.category = request.POST["category"]
            post.poster = request.FILES.get("poster",post.poster)
            post.save()
            return redirect("blog:post_detail_view", post_id=post.id)
        except Exception as e:
            print(e)

    
    return render(request, 'blog/update_post.html', {"post" : post, "categories" : Post.categories.choices})


def delete_post_view(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("blog:index")


# def search_page(request):
#     query = request.GET.get('query')  
#     if query:
#         posts = Post.objects.filter(title__icontains=query)
#     else:
#         posts = Post.objects.all()

#     return render(request, 'blog/search.html', {'posts': posts})


def search_page(request):
    query = request.GET.get('query')
    publish_date = request.GET.get('publish_date')

    posts = Post.objects.all()

    if query:
        posts = posts.filter(title__icontains=query)

    if publish_date:
        try:
            publish_date = datetime.strptime(publish_date, '%Y-%m-%d')
            posts = posts.filter(published_at__date=publish_date.date())
        except ValueError:
            pass

    return render(request, 'blog/search.html', {'posts': posts})