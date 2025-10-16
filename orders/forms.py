from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'postal_code', 'city']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'address': 'آدرس کامل',
            'postal_code': 'کد پستی',
            'city': 'شهر',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md'}),
            'address': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-md', 'rows': 3}),
            'postal_code': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md'}),
            'city': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md'}),
        }
