"""
URL configuration for industrial_mixer_project project.
"""
# بازگشت به ادمین پیش‌فرض جنگو
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views as shop_views 

urlpatterns = [
    # بازگشت به ادمین پیش‌فرض
    path('admin/', admin.site.urls),
    
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('ai/', include('ai_assistant.urls', namespace='ai_assistant')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('pages/', include('pages.urls', namespace='pages')),

    path('shop/', include('shop.urls', namespace='shop')), 
    path('', shop_views.home_view, name='home'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

