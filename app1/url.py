from app1.views import *
from django.urls import path

app_name='Baby'
urlpatterns=[
    path('Nvn/',Nvn,name='Nvn'),
]