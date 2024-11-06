from django.urls import path
from to_do.views import *
app_name='to_do'

urlpatterns = [
    path('',Home,name='Home'),
    path('Home',Home,name='Home'),
    path('Task/',Task,name='Task'),
]