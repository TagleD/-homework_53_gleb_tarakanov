from django.contrib import admin
from webapp.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'detailed_description', 'status', 'ended_at')
    list_filter = ('id', 'title', 'description', 'detailed_description', 'status', 'ended_at')
    search_fields = ('id', 'title', 'description', 'detailed_description', 'status', 'ended_at')
    fields = ('id', 'title', 'description', 'detailed_description', 'status', 'ended_at')
    readonly_fields = ('id', 'title', 'description', 'detailed_description', 'status', 'ended_at')


admin.site.register(Task, TaskAdmin)
