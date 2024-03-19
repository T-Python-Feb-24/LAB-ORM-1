from django.shortcuts import redirect, render
from django.http import HttpRequest, QueryDict
from .models import Post
from django.core.paginator import Paginator
# Create your views here.


def post_view(request: HttpRequest):
    posts = Post.objects.all().order_by('-published_at')[0:3]
    return render(request, "main/index.html", {"posts": posts})


def search(req: QueryDict):
    posts = Post.objects.all()
    if "title" in req:
        posts = posts.filter(title__contains=req["title"])
    if "cat" in req:
        posts = posts.filter(category=req["cat"])
        active_cat = req["cat"]
    else:
        active_cat = "All"
    if "date" in req and len(req["date"]) > 4:
        posts = posts.filter(published_at__startswith=req["date"])

    pages = Paginator(posts, per_page=3)
    if "page" in req:
        if int(req.get("page")) in pages.page_range:
            posts = pages.get_page(req.get("page"))
    else:
        posts = pages.get_page(1)
    return pages, posts, active_cat


def all_posts_view(request: HttpRequest):
    pages, posts, active_cat = search(request.GET)
    print(pages.count)
    return render(request, "main/all_posts.html",
                  {"posts": posts, "pages": pages, "active_cat": active_cat,
                   "categories": Post.category_choices.choices})


def add_post_view(request: HttpRequest):

    if request.method == "POST":
        if request.FILES.get("poster") != None:
            poster = request.FILES.get("poster")
            new_post = Post(
                title=request.POST.get("title"),
                category=request.POST.get("category"),
                content=request.POST.get("content"),
                is_published=request.POST.get("is_published", False),
                poster=request.FILES.get("poster"))
        else:
            new_post = Post(
                title=request.POST.get("title"),
                category=request.POST.get("category"),
                content=request.POST.get("content"),
                is_published=request.POST.get("is_published", False))
        new_post.save()
        return redirect("main:post_view")

    return render(request, "main/add_post.html", {"categories": Post.category_choices.choices})


def post_detail_view(request: HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, "404.html")
    except Exception as e:
        print(e)

    return render(request, "main/post_detail.html", {"post": post})


def update_post_view(request: HttpRequest, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        if request.method == "POST":
            post.title = request.POST.get("title")
            post.content = request.POST.get("content")
            post.category = request.POST.get("category")
            post.is_published = request.POST.get("is_published", False)
            if request.FILES.get("poster") != None:
                post.poster = request.FILES.get("poster")
            post.save()
            return redirect("main:post_detail_view", post_id)
        return render(request, 'main/update_post.html', {"post": post,
                                                         "categories": Post.category_choices.choices})
    except Post.DoesNotExist:
        return render(request, "404.html")
    except Exception as e:
        print(e)


def delete_post_view(request: HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Post.DoesNotExist:
        return render(request, "404.html")
    except Exception as e:
        print(e)

    return redirect("main:post_view")
