from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from django.contrib.auth.models import User


def index(request):
    user = User.objects.select_related('profile').get(id=1)
    print(user.services_set.all())
    print(user.educations_set.all())
    print(user.experiences_set.all())
    print(user.design_skills_set.all())
    print(user.coding_skills_set.all())
    # services = Services.objects.filter(user=1)
    # educations = Educations.objects.filter(user=1)
    # experiences = Experiences.objects.filter(user=1)
    # design_skills = Design_skills.objects.filter(user=1)
    # coding_skills = Coding_skills.objects.filter(user=1)
    context = {'user': user}
    return render(request, 'cv/index.html', context)


def resume(request):
    user = User.objects.get(id=1)
    educations = Educations.objects.filter(user=1)
    experiences = Experiences.objects.filter(user=1)

    design_skills = Design_skills.objects.filter(user=1)
    coding_skills = Coding_skills.objects.filter(user=1)
    context = {'educations': educations,
               'experiences': experiences, 'design_skills': design_skills, 'coding_skills': coding_skills}
    return render(request, 'cv/resume.html', context)
