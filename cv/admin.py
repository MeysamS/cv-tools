from django.contrib import admin
from .models import *
# Register your models here.


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
