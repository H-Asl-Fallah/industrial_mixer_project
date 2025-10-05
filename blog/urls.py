from django.urls import path
from . import views

# این متغیر برای استفاده از namespace در پروژه اصلی ضروری است
app_name = 'blog'

urlpatterns = [
    # آدرس اصلی وبلاگ که لیست مقالات را نمایش می‌دهد
    path('', views.article_list, name='article_list'),
    
    # آدرس مربوط به نمایش جزئیات یک مقاله
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]

