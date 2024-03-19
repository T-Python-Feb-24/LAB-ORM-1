from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.

def home(request: HttpRequest):
    posts = Post.objects.filter(is_published=True)[0:3]

    context = {
        "posts" : posts
    }
    return render(request,"main/home.html" , context)

def all_posts(request: HttpRequest):
     if "cat" in request.GET:
        posts = Post.objects.filter(category=request.GET["cat"])
     else:
        posts = Post.objects.all()
     
     return render(request,"main/all_posts.html", {"posts" : posts, "category" : Post.categories.choices})
     

def add(request: HttpRequest):

    if request.method =="POST":
        try:
            new_post = Post(
                title = request.POST["title"], 
                content = request.POST["content"],  
                is_published = request.POST.get("is_published", False),
                category = request.POST["category"],
                poster = request.FILES.get("poster", Post.poster.field.default)
            )

            new_post.save()

        except Exception as e:
            print(e)
        return redirect("main:home")

    return render(request,"main/add_post.html" , {"category" : Post.categories.choices})


def detail(request: HttpRequest , post_id):
     try:
            #getting a  post detail
            post = Post.objects.get(pk=post_id)
     except Post.DoesNotExist:
            return render(request,"main/not_found.html")
     except Exception as e:
            print(e)

     return render(request,"main/detail.html" , {"post" : post})



def update(request: HttpRequest ,post_id):
     post = Post.objects.get(pk=post_id)

     if request.method == "POST":
            try:
                post.title = request.POST["title"]
                post.content = request.POST["content"]
                post.is_published = request.POST.get("is_published", False)
                post.poster = request.FILES.get("poster", post.poster)
                post.category= request.POST["category"]

                post.save()

                return redirect("main:detail_page", post_id=post.id)
            except Post.DoesNotExist:
                return render(request, "main/not_found.html")
            except Exception as e:
                print(e)

     return render(request,"main/update.html" , {"post" : post , "category" : Post.categories.choices} )


def delete(request:HttpRequest, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Post.DoesNotExist:
        return render(request,"main/not_found.html")
    except Exception as e:
        print(e)

    return redirect("main:home")




def search(request:HttpRequest):
     if request.method == "GET":
          query=request.GET.get("query")
          if query:
            posts = Post.objects.filter(title__contains=query).order_by('-published_at')
            return render(request,"main/searchbar.html" , {"post" : posts})
          else:
            print("NO Reasult for this search")
            return render(request,"main/searchbar.html",{})