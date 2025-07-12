
from django.db import models
from users.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='project_leader',
        db_column='leader_id',
        null=False
    )
    created_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    number_of_panels = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
