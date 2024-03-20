from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','category','is_published','published_at']
    list_filter=['is_published','category']
admin.site.register(Post,PostAdmin)