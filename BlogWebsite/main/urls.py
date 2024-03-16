from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path('', views.post_view, name="post_view"),
    path('add/', views.add_post_view, name="add_post_view"),

]
