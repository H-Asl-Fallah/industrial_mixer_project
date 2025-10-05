from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    کلاس مدیریت برای مدل Article در پنل ادمین.
    """
    list_display = ('title', 'slug', 'status', 'publish')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    list_per_page = 20

