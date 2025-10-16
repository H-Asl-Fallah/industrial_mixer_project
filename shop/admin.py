from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for the Category model.
    """
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for the Product model.
    """
    # Added 'contact_for_price' to display and editing fields
    list_display = ['name', 'slug', 'category', 'price', 'available', 'contact_for_price', 'created']
    list_filter = ['available', 'created', 'updated', 'category', 'contact_for_price']
    list_editable = ['price', 'available', 'contact_for_price']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_per_page = 20
