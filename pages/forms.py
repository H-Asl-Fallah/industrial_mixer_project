from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام کامل شما'}),
            'email': forms.EmailInput(attrs={'placeholder': 'آدرس ایمیل'}),
            'subject': forms.TextInput(attrs={'placeholder': 'موضوع پیام'}),
            'message': forms.Textarea(attrs={'placeholder': 'پیام خود را اینجا بنویسید...', 'rows': 6}),
        }
        labels = {
            'name': 'نام شما',
            'email': 'ایمیل',
            'subject': 'موضوع',
            'message': 'پیام',
        }
