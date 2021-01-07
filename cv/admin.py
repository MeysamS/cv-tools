from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'پنل مدیریت سایت(رزومه ساز)'
@admin.register(Educations)
class EducationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    autocomplete_fields = ['user']


@admin.register(Design_skills)
class Design_skillsAdmin(admin.ModelAdmin):
    list_display = ['title', 'percent']

@admin.register(Coding_skills)
class Coding_skillsAdmin(admin.ModelAdmin):
    list_display = ['title', 'percent']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['bio']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name','email', 'message','jcreated_at', 'visited' ]
    search_fields = ('full_name','message')
    list_filter = (['created_at'])
