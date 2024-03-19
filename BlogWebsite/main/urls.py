from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_post, name='add_post'),
    path("post/detail/<post_id>/", views.post_detail, name="post_detail"),
    path("post/update/<post_id>/", views.update_post, name="update_post"),
    path("post/delete/<post_id>/", views.delete_post, name="delete_post"),
    path("post/all/", views.all_posts_view, name="all_posts_view"),
     path('search/', views.search_posts, name='search_posts')
]
