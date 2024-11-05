from django.urls import path
from to_do.views import *
app_name='home'

urlpatterns = [
    path('',Home,name='home'),
]