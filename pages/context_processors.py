from .models import ContactMessage

def unread_messages_count(request):
    """
    این تابع تعداد پیام‌های تماس خوانده نشده را شمارش کرده و
    آن را برای استفاده در تمام تمپلیت‌ها در دسترس قرار می‌دهد.
    این شمارش فقط برای کاربرانی که به پنل ادمین دسترسی دارند (staff) انجام می‌شود.
    """
    if request.user.is_authenticated and request.user.is_staff:
        count = ContactMessage.objects.filter(is_read=False).count()
        return {'unread_messages_count': count}
    return {}

