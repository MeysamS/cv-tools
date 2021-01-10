from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.contrib.auth.models import User


def index(request):
    context = {'articles': Article.objects.filter(
        status="p").order_by('-published_at'),
               'user': User.objects.get(pk=1)}
    return render(request, "blog/index.html", context)


def detail(request, slug):
    context = {'article': Article.objects.get(slug=slug), 'user': User.objects.get(pk=1)}
    return render(request, "blog/detail.html", context)


def category(request):
    context = {'categories': Category.objects.all(), 'user': User.objects.get(pk=1)}
    return render(request, "blog/categories.html", context)


def articles_category(request, slug):
    #  context = {
    #      "categories":
    #      get_object_or_404(Category, slug=slug, status=True),
    #      }
    context = {"categories": get_object_or_404(Category, slug=slug, status=True), 'user':User.objects.get(pk=1) }
    # context = {'categories': Category.objects.select_related('articles').filter(slug=slug , status=True)}
    return render(request, "blog/articles_category.html", context)
