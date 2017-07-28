from django.conf.urls import url
from .views import article

app_name = 'article'
urlpatterns = [
    url(r'^article/$', article, name='article'),
]
