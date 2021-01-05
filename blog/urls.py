from django.urls import path, re_path
from .views import index, detail, category, articles_category


app_name = 'blog'
urlpatterns = [
    path('categories/', category, name='category'),
    path('articles/', index, name='articles'),
    re_path(r'categories/(?P<slug>[-\w]+)/', articles_category, name='articles_category'),
    re_path(r'articles/(?P<slug>[-\w]+)/',  detail, name='detail'),
]
