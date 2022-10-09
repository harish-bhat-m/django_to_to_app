from django.shortcuts import render, HttpResponseRedirect
from .models import ToDoList
from .forms import ToDoListForm


def add_show(request):
    if request.method == 'POST':
        to_do_form = ToDoListForm(request.POST)
        if to_do_form.is_valid():
            l_task_name = to_do_form.cleaned_data['task_name']
            l_task_date = to_do_form.cleaned_data['task_date']
            l_task_status = to_do_form.cleaned_data['task_status']
            task_object = ToDoList(task_name=l_task_name, task_date=l_task_date, task_status=l_task_status)
            task_object.save()
            
            ## To directly save the form. This is also used to save
            #to_do_form.save()
            to_do_form = ToDoListForm()
            #to_do_list_record =  ToDoList.objects.all()
    else:
        to_do_form = ToDoListForm()
    to_do_list_record = ToDoList.objects.filter(task_status__in = ['to_do','in_progress'])
    return render(request, 'to_do/add_show.html', {'form':to_do_form,\
         'to_do_list':to_do_list_record})


def delete_task(request, id):
    if request.method == "POST":
        del_obj = ToDoList.objects.get(pk=id)
        del_obj.delete()
        return HttpResponseRedirect('/')

def complete_task(request, id):
    comp_obj = ToDoList.objects.get(pk=id)
    comp_obj.task_status = "complete"
    comp_obj.save()
    return HttpResponseRedirect('/')