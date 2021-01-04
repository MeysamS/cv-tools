from django.contrib import admin
from blog.models import Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','slug','published_at','status']
    list_filter = ('published_at','status')
    search_fields  = ('title','description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status','-published_at']