from django.urls import path
from . import views

urlpatterns = [
    path('', views.init),
    path('index', views.index),
    path('all-projects', views.allProjects, name='all-projects'),
    path('add-project', views.projectAdd, name='project-add'),
    path('project/<project_id>', views.project_detail),
    path('add-issue', views.issueAdd, name='issue-add'),
    path('issue/<issue_id>', views.issue_detail, name='issue'),
    path('issue-update/<issue_id>/<issue_position>/', views.issue_update, name='issue-update'),

]