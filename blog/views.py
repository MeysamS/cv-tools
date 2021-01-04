from django.shortcuts import render
from .models import Article


def index(request):
    context = {'articles': Article.objects.all()}
    return render(request, "blog/index.html" ,context)
