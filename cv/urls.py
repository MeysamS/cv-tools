from django.urls import path
from .views import index, resume

app_name = 'home'

urlpatterns = [
    # path('', ProfileListView.as_view(), name='index'),
    path('', index, name='index'),
    path('resume/', resume, name='resume')
]
