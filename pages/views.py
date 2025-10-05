from django.shortcuts import render

def about_us_view(request):
    """
    این ویو صفحه "درباره ما" را نمایش می‌دهد.
    """
    return render(request, '../templates/about_us.html')

def contact_us_view(request):
    """
    این ویو صفحه "تماس با ما" را نمایش می‌دهد.
    """
    return render(request, '../templates/contact_us.html')
