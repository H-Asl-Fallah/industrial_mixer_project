from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def about_us_view(request):
    """
    این ویو صفحه "درباره ما" را نمایش می‌دهد.
    """
    return render(request, '../templates/about_us.html')

def contact_us_view(request):
    """
    این ویو صفحه "تماس با ما" را نمایش داده و پردازش می‌کند.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد. به زودی با شما تماس خواهیم گرفت.')
            return redirect('pages:contact_us')
    else:
        form = ContactForm()
    
    return render(request, '../templates/contact_us.html', {'form': form})
