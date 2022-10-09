from django import forms
from .models import ToDoList, STATUS_CHOICE

        

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['task_name', 'task_date', 'task_status']
        
        labels = {'task_name': 'Task Name', 'task_date':'Date', 'task_status':'Status'}

        error_messages = {
            'task_name':{'required':"Task must be entered"},
            'task_date':{'required':'Date is necessary'},
        }

        widgets = {
            'task_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the task here'}),          
            'task_date':forms.TextInput(attrs={'type':'date', 'class':'form-control'}),
            'task_status':forms.Select(choices=STATUS_CHOICE, attrs={'class':'form-control'})
        }