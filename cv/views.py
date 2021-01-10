from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed, HttpResponse
from .forms import Contact_us_send_Form
from django.contrib import messages


def index(request):
    user = User.objects.select_related('profile').get(id=1)
    context = {'user': user, 'title': user.get_full_name}
    return render(request, 'cv/index.html', context)


def resume(request):
    user = User.objects.get(id=1)
    # educations = Educations.objects.filter(user=1)
    # experiences = Experiences.objects.filter(user=1)
    #
    # design_skills = Design_skills.objects.filter(user=1)
    # coding_skills = Coding_skills.objects.filter(user=1)
    # context = {'user': user, 'educations': educations,
    #            'experiences': experiences, 'design_skills': design_skills, 'coding_skills': coding_skills}
    context = {'user': user}
    return render(request, 'cv/resume.html', context)


def contact_us(request):
    return render(request, "cv/contact_us.html")


def contact_us_sendmessage(request):
    if request.method == "POST":
        form = Contact_us_send_Form(request.POST)
        if form.is_valid():
            ContactUs.objects.create(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            messages.success(
                request, 'پیام شما به مدیر سایت با مفقیت ارسال شد.')
    else:
        form = Contact_us_send_Form()

    return render(request, "cv/contact_us.html", {'form': form})
    # return HttpResponseNotAllowed('post')
