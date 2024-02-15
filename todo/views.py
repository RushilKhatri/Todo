from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import task

def addtask(request):
    tasks=request.POST['task']
    task.objects.create(task=tasks)
    return redirect('home')
