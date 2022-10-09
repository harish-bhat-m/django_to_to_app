from django.db import models
from datetime import datetime

STATUS_CHOICE = (
    ('to_do', 'To Do'),
    ('in_progress', 'In Progress'),
    ('complete', 'Complete')
)

class ToDoList(models.Model):
    task_name = models.CharField(max_length=50)
    task_date = models.DateTimeField(default=datetime.now())
    task_status = models.CharField(max_length=15, choices=STATUS_CHOICE, default='to_do')

    def get_status(self):
        for ind_tupple in STATUS_CHOICE:
            if ind_tupple[0] == self.task_status:
                return ind_tupple[1]