from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about-us/', views.about_us_view, name='about_us'),
    path('contact-us/', views.contact_us_view, name='contact_us'),
]
