from django.urls import path
from . import views

app_name = 'ai_assistant'

urlpatterns = [
    # آدرس صفحه اصلی چت
    path('', views.chat_view, name='chat'),
    # آدرس API داخلی برای دریافت پاسخ از هوش مصنوعی
    path('get-response/', views.get_ai_response, name='get_ai_response'),
]