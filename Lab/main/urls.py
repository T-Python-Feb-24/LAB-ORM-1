from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
   path('',views.Blog,name="home"),
   path("add/" , views.add_blog,name="add_page"),
]