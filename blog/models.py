from django.db import models
from django.utils import timezone
from extensions.myjalali import jalali_converter



class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name='آدرس دسته بندی',
                            help_text="این فیل به صورت خودکار زمانی که عنوان را وارد میکنید پر خواهد شد")  
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    image = models.ImageField(upload_to="categories", verbose_name="تصویر برای دسته بندی",null=True,blank=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']
    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیشنویس'), ('p', 'منتشر شده')
    )
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name='آدرس لینک',
                            help_text="این فیل به صورت خودکار زمانی که عنوان را وارد میکنید پر خواهد شد")
    category = models.ManyToManyField(Category, verbose_name="انتخاب دسته بندی مورد نظر",related_name="articles")
    # category.help_text = 'با نگه داشتن کلید ctrl می توانید انتخاب های بیشتری داشته باشید'
    description = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to='blog', verbose_name="تصویر")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

    def jpublished_at(self):
        return jalali_converter(self.published_at)
    jpublished_at.short_description = "زمان انتشار"

