from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index_view, name="index.view"),
    path("new/post/", views.add_post_view, name="add_post"),
]