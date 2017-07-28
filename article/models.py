# -*- coding: utf-8 -*-
import markdown2
from django.db import models
from markdownx.models import MarkdownxField


class Category(models.Model):
    name = models.CharField('名称', max_length=32)
    note = models.CharField('备注', max_length=128, blank=True)

    def __str__(self):
        return self.name


class MarkdownField(models.Model):
    """
    Markdown 文本
    """
    title = models.CharField('标题', max_length=32)
    markdown = models.TextField('Markdown', max_length=4096)
    html = models.TextField('HTML', max_length=4096, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.html = markdown2.markdown(self.markdown)
        super(MarkdownField, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField('标题', max_length=256)
    summary = models.CharField('概述', max_length=1024, default='')
    date = models.DateTimeField('日期', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='分类', default=None)
    content = MarkdownxField()

    def __str__(self):
        return self.title
