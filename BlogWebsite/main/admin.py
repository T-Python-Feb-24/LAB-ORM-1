from django.contrib import admin
from  .models import Post
# Register your models here.


class PublisherAdmin(admin.ModelAdmin):
    list_display= ('title', 'category', 'is_published', 'published_at')

    list_filter= ('published_at','category',)

admin.site.register(Post, PublisherAdmin)