from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('new/post', views.add_post_page, name = 'add_post_page'),
    path("post/detail/<post_id>/", views.post_detail_page, name="post_detail_page"),
    path("post/update/<post_id>/", views.update_post_page, name="update_post_page"),
    path("post/delete/<post_id>/", views.delete_post_page, name="delete_post_page"),
    path("post/all/", views.all_posts_page, name="all_posts_page")

]