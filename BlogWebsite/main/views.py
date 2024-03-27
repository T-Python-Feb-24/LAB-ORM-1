from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
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
    
    #calculate the page content
    limit = 3
    pages_count = [str(n) for n in range(1, round(posts.count()/limit)+1)] #use list comprehension to convert number to string number
    start = (int(request.GET.get("page", 1))-1)*limit
    end = (start)+limit

    print(list(pages_count))


    #apply the limit/slicing
    posts = posts[start:end]

    # print(start, end)

    return render(request, "main/all_posts.html", {"posts" : posts, "categories" : Post.categories.choices, "pages_count":pages_count})

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



def posts_search_view(request:HttpRequest):
    posts = []

    if "search" in request.GET:
        posts = Post.objects.filter(title__contains=request.GET["search"])

    if "date" in request.GET and len(request.GET["date"]) > 4:
        first_date = date.fromisoformat(request.GET["date"])
        end_date = first_date + timedelta(days=1)
        posts = posts.filter(published_at__gte=first_date, published_at__lt=end_date)


    return render(request, "main/search_page.html", {"posts" : posts})

