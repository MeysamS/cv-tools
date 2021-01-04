from django.urls import path, re_path
from .views import index, detail


app_name = 'blog'
urlpatterns = [
    path('articles/', index, name='articles'),
    re_path(r'articles/(?P<slug>[-\w]+)/',  detail, name='detail'),
]
