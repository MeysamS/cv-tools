from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from extensions.customFieldTypes import IntegerRangeField
from extensions.validator_files import validate_file_extension
from django.utils import timezone

class Educations(models.Model):
    '''
        تحصیلات
    '''
    title = models.CharField(max_length=255, verbose_name="عنوان")
    date_of_date = models.CharField(max_length=15,verbose_name="از تاریخ تا تاریخ")
    description = models.TextField(max_length=1000,verbose_name="توضیحات")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تحصیلات'
        verbose_name_plural = "تحصیلات"


# تجربیات
class Experiences(models.Model):
    title = models.CharField(max_length=255,verbose_name="عنوان")
    date_of_date = models.CharField(max_length=15,verbose_name="از تاریخ تا تاریخ")
    description = models.TextField(max_length=1000,verbose_name="توضیحات")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'تجربیات'
        verbose_name_plural = "تجربیات"


# مهارت های طراحی
class Design_skills(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    percent = IntegerRangeField(
        min_value=1, max_value=100, verbose_name="میزان مهارت (به درصد)", help_text="میزان درجه مهارت شما از 1 الی 100")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "مهارت های طراحی"
        verbose_name_plural = "مهارت های طراحی"

# مهارت های کد نویسی


class Coding_skills(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    percent = IntegerRangeField(
        min_value=1, max_value=100, verbose_name="میزان مهارت (به درصد)", help_text="میزان درجه مهارت شما از 1 الی 100")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "مهارت های کدنویسی"
        verbose_name_plural = "مهارت های کدنویسی"

    def __str__(self):
        return self.title

# کارهایی که انجام میدهم


class Services(models.Model):
    title = models.CharField(max_length=255,verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    icons = models.ImageField(upload_to='myicons',verbose_name="آیکن")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "خدمات"
        verbose_name_plural = "کارهایی که انجام میدهم"

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    bio = models.TextField(max_length=1000, blank=True, verbose_name="درباره من")
    location = models.CharField(max_length=30, blank=True,verbose_name="آدرس")
    brith_date = models.DateField(null=True, blank=True,verbose_name="تاریخ تولد")
    phone_number = models.CharField(max_length=11,verbose_name="تلفن همراه")
    avatar = models.ImageField(upload_to='avatar', null=True,verbose_name="تصویر پروفایل")
    resume_file = models.FileField(upload_to='resumeFile', null=True, validators=[
                                   validate_file_extension],verbose_name="فایل رزومه", help_text="پسوند فایل فقط باید شامل نوع pdf و یا  word باشد")
    job_title = models.CharField(max_length=200, verbose_name="عنوان شغلی",null=True,blank=True)

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل"


class Article(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),('p','Published')
    )
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length=100 )
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='blog')
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)