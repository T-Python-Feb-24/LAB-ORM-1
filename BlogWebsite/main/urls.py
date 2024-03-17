from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path('', views.post_view, name="post_view"),
    path('add/', views.add_post_view, name="add_post_view"),
    path("post/detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("post/update/<post_id>/", views.update_post_view, name="update_post_view"),
    path("post/delete/<post_id>/", views.delete_post_view, name="delete_post_view")

]
