from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('new/post', views.add_post_page, name = 'add_post_page'),
]