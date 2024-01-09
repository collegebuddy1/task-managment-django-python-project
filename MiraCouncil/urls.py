"""MiraCouncil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from MiraTask.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.views, name='homepage'),

    path('tasks', TaskPage.views, name='taskpage'),
    path('tasks/addTask', TaskPage.addTask, name='addTask'),
    path('tasks/deleteTask/<id>', TaskPage.deleteTask, name='deleteTask'),
    path('tasks/updateTask/id=<id>&status=<status>', TaskPage.updateTask, name='updateTask'),

    path('account/', include('allauth.urls'), name='login'),
    path('sign-out', Auth.logout, name='logout'),
]
