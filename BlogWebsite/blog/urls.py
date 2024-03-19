from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name='index'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path("post/detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("post/update/<post_id>/", views.update_post_view, name="update_post_view"),
    path("post/delete/<post_id>/", views.delete_post_view, name="delete_post_view"),
    path("post/all/", views.all_posts_view, name="all_posts_view"),
    path('search/',views.search_page, name="search_page"),


]
