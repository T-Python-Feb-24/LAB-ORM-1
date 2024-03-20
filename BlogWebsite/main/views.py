from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post
from datetime import date, timedelta



def home_view(request: HttpRequest):
    #query
    print(request.GET)

    #limit باستخدام Slicing  بناء على تاريخ الارسال يرتب اول ثلاث بس
    posts = Post.objects.all().order_by('-published_at')[0:3]

    #get all entries insisde database
    #posts = Post.objects.all()
    #context = {
        #"posts" : posts}

    return render(request, "main/home.html", {"posts" : posts})




def add_blog_view(request: HttpRequest):

    
    #adding a new entry
       
    if request.method == "POST":
        try:
         new_blog = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST.get("is_published", False),category=request.POST["category"] ,poster=request.FILES["poster"])
         new_blog.save()
         return redirect("main:home_view")
        except Exception as e:
            print(e)
    return render(request, "main/add.html", {"categories" : Post.categories.choices})
        
       

def detail_view(request:HttpRequest, post_id):

    try:
        #getting a  post detail
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, "main/404.html")
        
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
            post.category = request.POST["category"]
            post.poster = request.FILES.get("poster", post.poster)
            post.save()
            return redirect("main:detail_view", post_id=post.id)
        except Exception as e:
            print(e)

    
    return render(request, 'main/update.html', {"post" : post, "categories" : Post.categories.choices})


def delete_view(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("main:home_view")

def all_view(request:HttpRequest):

    if "cat" in request.GET:
      posts = Post.objects.filter(category=request.GET["cat"])
    else:
      posts = Post.objects.all()

    return render(request, "main/all.html", {"posts" : posts, "categories" : Post.categories.choices})

def search_view(request:HttpRequest):
    posts = []

    if "search" in request.GET:
        posts = Post.objects.filter(title__contains=request.GET["search"])
    if "search" in request.GET:
        posts = Post.objects.filter(category__contains=request.GET["search"])

    if "date" in request.GET and len(request.GET["date"]) > 4:
        first_date = date.fromisoformat(request.GET["date"])
        end_date = first_date + timedelta(days=1)
        posts = posts.filter(published_at__gte=first_date, published_at__lt=end_date)


    return render(request, "main/search.html", {"posts" : posts})


   