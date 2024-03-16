from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.home_view, name="home_view"),
    path("new/blog/", views.add_blog_view, name="add_blog_view"),
]