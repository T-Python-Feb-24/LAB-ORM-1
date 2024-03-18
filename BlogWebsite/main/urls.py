from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.home_view, name="home_view"),
    path("new/blog/", views.add_blog_view, name="add_blog_view"),
    path("post/detail/<post_id>/", views.detail_view, name="detail_view"),
    path("post/update/<post_id>/", views.update_view, name="update_view"),
    path("post/delete/<post_id>/", views.delete_view, name="delete_view"),
    path("post/all/", views.all_view, name="all_view"),
    path(r'^home/$',views.search_view, name="search_view" )
]
