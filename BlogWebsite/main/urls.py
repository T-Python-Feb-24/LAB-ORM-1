from django.urls import path
from .import views 

app_name="main"

urlpatterns = [
    path("",views.home_page,name='home_page'),
    path("new/post",views.add_post,name="add_post"),
    path("post/detail/<post_id>/",views.post_detail,name="post_detail"),
    path("post/delete/<post_id>/",views.delete_post,name="delete_post"),
    path("post/update/<post_id>/",views.update_post,name="update_post"),
    path("all/posts/",views.all_posts,name="all_posts"),
    path("search/",views.search_page,name="search_page"),
]
