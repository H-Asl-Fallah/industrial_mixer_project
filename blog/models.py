from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'پیش‌نویس'),
        ('published', 'منتشر شده'),
    )
    title = models.CharField(max_length=250, verbose_name="عنوان")
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name="اسلاگ (آدرس)")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="نویسنده")
    body = models.TextField(verbose_name="متن مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="وضعیت")
    image = models.ImageField(upload_to='articles/%Y/%m/%d/', blank=True, verbose_name="تصویر")

    objects = models.Manager()  # مدیر پیش‌فرض
    published = PublishedManager()  # فقط مقالات منتشر شده

    class Meta:
        ordering = ('-publish',)
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

