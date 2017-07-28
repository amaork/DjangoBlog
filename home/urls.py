from django.conf.urls import url
from .views import homepage, about

app_name = 'homepage'
urlpatterns = [

    url(r'^$', homepage, name='homepage'),
    url(r'^home/$', homepage, name='homepage'),
    url(r'^about/$', about, name='about'),
]