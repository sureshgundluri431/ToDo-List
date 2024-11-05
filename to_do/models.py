from django.db import models

# Create your models here.

STATUS_CHOICES=[
    ('not_started','Not Started'),
    ('in_progress','In Progress'),
    ('completed','Completed'),
    ('on_hold','On Hold')
]

class Task(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100,unique=True)
    description=models.TextField()
    created_Date=models.DateTimeField(auto_now_add=True)
    updated_Date=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=20 ,choices=STATUS_CHOICES, default='Not Started')

    def __str__(self):
        return self.title

