from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),('p','Published')
    )
    title=models.CharField(max_length=200,verbose_name="عنوان")
    slug = models.SlugField(max_length=100,unique=True, allow_unicode=True ,verbose_name='آدرس لینک', help_text="این فیل به صورت خودکار زمانی که عنوان را وارد میکنید پر خواهد شد")
    description = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to='blog',verbose_name="تصویر")
    published_at = models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت")

    class Meta:
       verbose_name = "مقاله"
       verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title
    
