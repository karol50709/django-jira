from django.urls import path
from . import views

urlpatterns = [
    path('', views.init),
    path('index', views.index),
    path('all-projects', views.allProjects),
    path('add-project', views.projectAdd, name='project-add'),
    path('project/<project_id>', views.project_detail),
    path('add-issue', views.issueAdd, name='issue-add')

]