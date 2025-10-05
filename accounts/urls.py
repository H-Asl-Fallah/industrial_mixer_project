from django.urls import path
from . import views

# این متغیر برای استفاده از namespace در پروژه اصلی ضروری است
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
]

