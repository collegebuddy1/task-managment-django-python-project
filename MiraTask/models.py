from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    todo = 'to-do'
    doing = 'doing'
    done = 'done'
    STATUS = [(todo, 'to-do'), (doing, 'doing'), (done, 'done')]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=5, choices=STATUS, default=todo, null=False, blank=False)
    deadline = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)