from django import forms
from .views import Project

class ProjectForm(forms.Form):
    class Meta:
      model = Project
      fields = '__all__'