from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project, Issue
from .forms import ProjectForm

# Create your views here.

def init(request):
    return HttpResponse('XYZ')

def index(request):
    context = {"projects": Project.objects.all()}
    return render(request, "myapp/index.html", context)   

def allProjects(request):
    context = {"projects": Project.objects.all()}
    return render(request, "myapp/project_list.html", context)  

def projectAdd(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        p = Project(project_name = form.data['project_name'], project_prefix = form.data['project_prefix'], project_desc = form.data['project_desc'])
        p.save()
    form = ProjectForm()
    return render(request, 'myapp/project_add.html',{'form': form})

def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    issues = Issue.objects.select_related().filter(issue_project = project_id)
    context = {
                "project": project,
                "issues": issues}
    return render(request, 'myapp/project_details.html',context)
