from django.urls import path
from webapp.views.base import index_view
from webapp.views.tasks import tasks_view, add_view, detail_view

urlpatterns = [
    path('', index_view, name='index'),
    path('tasks', tasks_view, name='tasks_view'),
    path('task/<int:pk>', detail_view, name='task_detail'),
    path('tasks/add', add_view, name='task_add')
]
