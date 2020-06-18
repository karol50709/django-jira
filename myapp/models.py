from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_prefix = models.CharField(max_length=10)
    project_desc = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.project_name)

class Issue(models.Model):
    issue_name = models.CharField(max_length=100)
    issue_level = models.IntegerField()
    issue_description = models.CharField(max_length=100)
    issue_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.issue_name)