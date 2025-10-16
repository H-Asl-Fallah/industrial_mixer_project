from django.db import models
from django.conf import settings
from shop.models import Product

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name="کاربر")
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    address = models.CharField(max_length=250, verbose_name="آدرس")
    postal_code = models.CharField(max_length=20, verbose_name="کد پستی")
    city = models.CharField(max_length=100, verbose_name="شهر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")
    paid = models.BooleanField(default=False, verbose_name="پرداخت شده")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش‌ها'

    def __str__(self):
        return f'سفارش {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name="محصول")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت")
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
