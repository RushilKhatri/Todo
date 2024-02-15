from django.shortcuts import render
from todo.models import task


def home(request):
    tasks=task.objects.filter(is_completed=False).order_by('-updated_at') #- indicates descending order
    tasks_complete= task.objects.filter(is_completed=True)
    context={
        'task': tasks,
        'complete_task':tasks_complete
    }
    return render(request, "Home.html", context)