# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from .models import Category, Article


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'note']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'date', 'category', 'content')
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
