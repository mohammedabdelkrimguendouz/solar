
from django.db import models
from projects.models import Project

class Progress(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='progress')
    report_date = models.DateField()
    panels_installed = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.project.name} - {self.report_date} - {self.panels_installed} panels"
