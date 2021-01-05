from django.shortcuts import render, get_object_or_404
from .models import Article, Category


def index(request):
    context = {'articles': Article.objects.filter(
        status="p").order_by('-published_at')}
    return render(request, "blog/index.html", context)


def detail(request, slug):
    context = {'article': Article.objects.get(slug=slug)}
    return render(request, "blog/detail.html", context)


def category(request):
    context = {'categories': Category.objects.all()}
    return render(request, "blog/categories.html", context)


def articles_category(request, slug):
    #  context = {
    #      "categories": 
    #      get_object_or_404(Category, slug=slug, status=True), 
    #      }
    context = {"categories": get_object_or_404(Category, slug = slug, status=True),}
    # context = {'categories': Category.objects.select_related('articles').filter(slug=slug , status=True)}
    return render(request, "blog/articles_category.html", context)
