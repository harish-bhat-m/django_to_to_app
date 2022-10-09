from django.contrib import admin
from .models import ToDoList

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_date', 'task_status')

