from django.contrib import admin
from .models import BlogInfo


# Register your models here.
class BlogInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slogan', 'wechat', 'email', 'github']


admin.site.register(BlogInfo, BlogInfoAdmin)
