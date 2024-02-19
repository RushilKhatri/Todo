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

def mark_as_undone(request,pk):
    tassk_n= get_object_or_404(task, pk=pk)
    tassk_n.is_completed=False
    tassk_n.save()
    return redirect('home')

def edit_task(request, pk):
    edit_t= get_object_or_404(task, pk=pk)
    if request.method == 'POST':
        updated = request.POST['task']
        edit_t.task = updated
        edit_t.save()
        return redirect('home')
    else:
        context={
            'edit_t':edit_t
        }

        return render(request, 'edit.html', context)
    
def delete_task(request, pk):
    dele= get_object_or_404(task,pk=pk )
    dele.delete()
    return redirect('home')