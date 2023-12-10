from django import forms
from .models import TaskModel
from datetime import datetime
from category.models import TaskCategory

class TaskModelForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=TaskCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'task_Assign_Date': forms.DateInput(attrs={'type': 'date'}),
        }