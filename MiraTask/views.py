from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
class HomePage():
    def views(request):
        return render(request, 'index.html')

class Auth():
    def logout(request):
        logout(request)
        return redirect('homepage')

class TaskPage():
    @login_required
    def views(request):
        taskData = Task.objects.all().order_by('-createdDate')
        return render(request, 'taskPage/index.html', {'tasks': taskData})

    def addTask(request):
        taskName = request.POST['taskname']
        deadline = request.POST['deadline']

        if not deadline:
            deadlineNull = None
        else:
            deadlineNull = deadline

        Task.objects.create(
            name = taskName,
            deadline = deadlineNull,
            author = request.user,
        )
        return redirect('/tasks')

    def deleteTask(request, id):
        Task.objects.filter(id = id).delete()
        return redirect('/tasks')

    def updateTask(request, status, id):
        task = Task.objects.get(id = id)
        task.status = status
        task.save()
        return redirect('/tasks')