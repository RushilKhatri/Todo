from django.shortcuts import render
from todo.models import task


def home(request):
    tasks=task.objects.filter(is_completed=False).order_by('-updated_at') #- indicates descending order
    context={
        'task': tasks
    }
    return render(request, "Home.html", context)