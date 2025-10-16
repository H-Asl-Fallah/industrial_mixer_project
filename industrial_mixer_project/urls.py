from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from shop.views import home_view

urlpatterns = [
    # URLs that should not be multilingual
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    # This URL provides the 'set_language' view
    path('i18n/', include('django.conf.urls.i18n')),
]

# URLs that should be multilingual
urlpatterns += i18n_patterns(
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('profile/', include('profiles.urls', namespace='profiles')),
    path('ai_assistant/', include('ai_assistant.urls', namespace='ai_assistant')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('', home_view, name='home'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

