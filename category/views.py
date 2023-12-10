from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.



def add_category(request):
    form = forms.TaskCategoryForm()
    if request.method == 'POST':
        form = forms.TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'add_category.html', {'form': form})


def edit_category(request, category_id):
    category = models.TaskCategory.objects.get(pk=category_id)
    form = forms.TaskCategoryForm(instance=category)
    if request.method == 'POST':
        form = forms.TaskCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'add_category.html', {'form': form})