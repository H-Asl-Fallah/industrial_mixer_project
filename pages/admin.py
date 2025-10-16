from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    کلاس مدیریت برای نمایش پیام‌های تماس در پنل ادمین.
    """
    list_display = ('subject', 'name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_per_page = 20
    # فیلدهای زیر در حالت مشاهده جزئیات، فقط خواندنی هستند
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

    def has_add_permission(self, request):
        # این متد امکان افزودن پیام جدید از طریق پنل ادمین را غیرفعال می‌کند
        return False

    def has_delete_permission(self, request, obj=None):
        # این متد امکان حذف پیام‌ها را برای امنیت بیشتر فراهم می‌کند (می‌توانید به True تغییر دهید)
        return True

