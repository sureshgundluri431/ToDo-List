from to_do.models import *
from django import forms
class Task_Form(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'
        