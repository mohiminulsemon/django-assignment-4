from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def add_task(request):
    form = forms.TaskModelForm()
    if request.method == 'POST':
        form = forms.TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, task_id):
    task = models.TaskModel.objects.get(pk=task_id)
    form = forms.TaskModelForm(instance=task)
    if request.method == 'POST':
        form = forms.TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'add_task.html', {'form': form})

def delete_task(request, task_id):
    task = models.TaskModel.objects.get(pk=task_id)
    task.delete()
    return redirect('show_tasks')