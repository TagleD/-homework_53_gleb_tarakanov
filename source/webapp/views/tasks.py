from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.db import DataBase
from webapp.models import Task

def tasks_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html', context=context)

# def detail_view(request):
#     task_pk = request.GET.get('pk')
#     task = Task.objects.get(pk=task_pk)
#     context = {'task': task}
#     return render(request, 'task_detail.html', context=context)

def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_detail.html', context=context)

def add_view(request: WSGIRequest):
    if request.method == 'GET':
        context = {'choices': DataBase.choices}
        return render(request, 'add_task.html', context=context)
    task_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'detailed_description': request.POST.get('detailed_description'),
        'status': DataBase.get_status(request.POST.get('status')),
        'ended_at': request.POST.get('date')
    }
    task = Task.objects.create(**task_data)
    return redirect('task_detail', pk=task.pk)

