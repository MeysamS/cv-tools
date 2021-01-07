from django.urls import path, include
from .views import index, resume, contact_us, contact_us_sendmessage

app_name = 'home'

urlpatterns = [
    # path('', ProfileListView.as_view(), name='index'),
    path('', index, name='index'),
    # Third-Party urls
    path('resume/', resume, name='resume'),
    path('contact-us/', contact_us, name='contact_us'),
    path('contact-us/send', contact_us_sendmessage, name='send'),
]
