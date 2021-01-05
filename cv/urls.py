from django.urls import path, include
from .views import index, resume

app_name = 'home'

urlpatterns = [
    # path('', ProfileListView.as_view(), name='index'),
    path('', index, name='index'),
    # Third-Party urls
    path('resume/', resume, name='resume')
]
