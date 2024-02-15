from django.contrib import admin
from .models import task

class taskadmin(admin.ModelAdmin):
    list_display=('task','is_completed','updated_at')

admin.site.register(task, taskadmin)
