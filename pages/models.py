from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام فرستنده")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=200, verbose_name="موضوع")
    message = models.TextField(verbose_name="متن پیام")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده")

    class Meta:
        verbose_name = "پیام دریافتی"
        verbose_name_plural = "پیام‌های تماس باما "
        ordering = ('-created_at',)

    def __str__(self):
        return f"پیام از طرف {self.name} با موضوع: {self.subject}"
