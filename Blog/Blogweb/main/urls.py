from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
   path("",views.home,name="home"),
   path("add/",views.add,name="add_page"),
   path("detail/<post_id>/",views.detail,name="detail_page"),
   path("update/<post_id>/",views.update,name="update_page"),
   path("update/<post_id>/",views.delete,name="delete_view"),
   path("all/", views.all_posts, name="all_posts"),
   path("saerch/",views.search,name="search_page"),
]