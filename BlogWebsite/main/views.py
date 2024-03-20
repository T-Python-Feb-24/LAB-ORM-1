from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def home_page(request: HttpRequest):
    
    # The field specified in a lookup has to be the name of a model field
    posts = Post.objects.filter(is_published = True)
    
    return render(request,'main/home_page.html',{"posts":posts})


def add_post(request : HttpRequest):
    
    if request.method == "POST":
        try:
            #creating instance (object) of Post class (Model) , and populate the attributes dynamically from the user input received in the request 
            new_post = Post(
                title = request.POST.get("title"),
                content = request.POST.get("content"),
                is_published = request.POST.get('is_published',False),
                poster = request.FILES["poster"],
                category = request.POST["category"]
            )
            
            # model.save() 
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
    
    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    
    return redirect("main:home_page")


def update_post(request : HttpRequest,post_id):
    
    post = Post.objects.get(pk=post_id)
    
    if request.method == "POST":
        
        try:
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.is_published = request.POST.get("is_published", False)
            post.poster = request.FILES.get("poster", post.poster)
            post.category = request.POST["category"]
            post.save()
            return redirect("main:post_detail", post_id = post.id)
        except Exception as e :
           print(e)
       
    return render(request,"main/update_post.html",{"post":post,"categories":Post.categories.choices})


def all_posts(request: HttpRequest):
        
    if "cat" in request.GET:
        posts = Post.objects.filter(category=request.GET["cat"])
    else:
        posts = Post.objects.all()

    return render(request,'main/all_posts.html',{"posts":posts ,"categories":Post.categories.choices})


def search_page(request: HttpRequest):
    
    if "search" in request.GET:
        posts = Post.objects.filter(title__contains=request.GET["search"])

    if "date" in request.GET and len(request.GET["date"]) > 4:
        first_date = date.fromisoformat(request.GET["date"])
        end_date = first_date + timedelta(days=1)
        posts = posts.filter(published_at__gte=first_date, published_at__lt=end_date)

    return render (request,"main/search_page.html",{"posts":posts})

