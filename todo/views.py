from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from todo.models import task

def addtask(request):
    tasks=request.POST['task']
    task.objects.create(task=tasks)
    return redirect('home')

def mark_as_done(request, pk):
    task_t= get_object_or_404(task, pk=pk)
    task_t.is_completed= True
    task_t.save()
    return redirect('home')