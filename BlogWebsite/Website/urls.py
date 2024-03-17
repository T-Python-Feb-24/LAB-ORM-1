from django.urls import path
from . import views

app_name = "Website"

urlpatterns  = [
    path("", views.index, name="index"),
    path("new/post/", views.add_post, name="add_post"),
    
]