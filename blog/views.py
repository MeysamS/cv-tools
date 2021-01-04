from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    context = { 'articles':Article.objects.all() }        
    return render(request, "blog/index.html", context)