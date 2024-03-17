from django.urls import path
from .import views 

app_name="main"

urlpatterns = [
    path("",views.home_page,name='home_page'),
    path("new/post",views.add_post,name="add_post"),
    
]
