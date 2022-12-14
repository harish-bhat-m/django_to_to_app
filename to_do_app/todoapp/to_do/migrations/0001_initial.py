# Generated by Django 3.2.15 on 2022-10-08 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('task_date', models.DateTimeField(default=datetime.datetime(2022, 10, 8, 15, 26, 13, 635052))),
                ('task_status', models.CharField(choices=[('to_do', 'To Do'), ('in_progress', 'In Progress'), ('complete', 'Complete')], default='to_do', max_length=15)),
            ],
        ),
    ]
