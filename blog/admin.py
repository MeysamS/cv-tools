from django.contrib import admin
from blog.models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug',
                    'jpublished_at', 'status', 'category_to_str']
    list_filter = ('published_at', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-published_at']

    def category_to_str(self, object):
        return ", ".join([category.title for category in object.category.all()])
    category_to_str.short_description = "دسته بندی"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'slug', 'status']
    list_display_links = ('title',)
    list_filter = (['status'])
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
