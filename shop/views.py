from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from blog.models import Article
# اضافه شد: برای دسترسی به فرم سبد خرید
from cart.forms import CartAddProductForm 

def home_view(request):
    latest_products = Product.objects.filter(available=True).order_by('-created')[:4]
    latest_articles = Article.objects.filter(status='published').order_by('-publish')[:3]
    
    context = {
        'latest_products': latest_products,
        'latest_articles': latest_articles,
    }
    return render(request, '../templates/home.html', context)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  '../templates/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug,
                                available=True)
    # اضافه شد: فرم افزودن به سبد خرید ایجاد و به قالب ارسال شد
    cart_product_form = CartAddProductForm()
    return render(request,
                  '../templates/product_detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

