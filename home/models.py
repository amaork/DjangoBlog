# -*- coding: utf-8 -*-
from django.db import models


class Navigation(object):
    def __init__(self, url, text):
        self.url = url
        self.text = text


# Create your models here.
class BlogInfo(models.Model):
    name = models.CharField('名称', max_length=32, default='')
    slogan = models.CharField('口号', max_length=64, default='')
    wechat = models.CharField('微信', max_length=16, default='')
    email = models.EmailField('邮箱', max_length=32, default='')
    github = models.CharField('Github', max_length=32, default='')
