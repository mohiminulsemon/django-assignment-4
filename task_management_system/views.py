from django.shortcuts import render
from task.models import TaskModel

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'base.html', {'tasks': tasks})