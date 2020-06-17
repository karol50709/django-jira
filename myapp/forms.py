from django import forms
from .models import Project

class ProjectForm(forms.Form):
    project_name = forms.CharField(label='Nazwa projektu',max_length=100)
    project_prefix = forms.CharField(label='Prefix projektu',max_length=10)
    project_desc = forms.CharField(label='Opis projektu',max_length=1000)
