from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'user__username']

admin.site.register(Task, TaskAdmin)

