from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('new/Post/', views.add_post_page, name='add_post_page'),
]