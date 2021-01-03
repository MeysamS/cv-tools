from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from extensions.customFieldTypes import IntegerRangeField
from extensions.validator_files import validate_file_extension


class Educations(models.Model):
    '''
        تحصیلات
    '''
    title = models.CharField(max_length=255)
    date_of_date = models.CharField(max_length=15)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "تحصیلات"


# تجربیات
class Experiences(models.Model):
    title = models.CharField(max_length=255)
    date_of_date = models.CharField(max_length=15)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "تجربیات"


# مهارت های طراحی
class Design_skills(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    percent = IntegerRangeField(
        min_value=1, max_value=100, verbose_name="میزان مهارت (به درصد)", help_text="میزان درجه مهارت شما از 1 الی 100")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "مهارت های طراحی"

# مهارت های کد نویسی


class Coding_skills(models.Model):
    title = models.CharField(max_length=255)
    percent = IntegerRangeField(min_value=1, max_value=100)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "مهارت های کدنویسی"

    def __str__(self):
        return self.title

# کارهایی که انجام میدهم


class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icons = models.ImageField(upload_to='myicons')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "کارهایی که انجام میدهم"

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    bio = models.TextField(max_length=1000, blank=True)
    location = models.CharField(max_length=30, blank=True)
    brith_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='avatar', null=True)
    resume_file = models.FileField(upload_to='resumeFile', null=True, validators=[
                                   validate_file_extension])

    class Meta:
        verbose_name_plural = "پروفایل"
