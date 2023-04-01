#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [
    # Create a task
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    # Retrieve task list
    path('', views.TaskListView.as_view(), name='task_list'),
    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='task_detail'),
    # Update a task
    re_path(r'^(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name='task_update'),
    # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete')

    # # Create a task
    # path('create/', views.task_create, name='task_create'),
    # # Retrieve task list
    # path('', views.task_list, name='task_list'),
    # # Retrieve single task object
    # re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    # # Update a task
    # re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # # Delete a task
    # re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),

]

'''In Class-based views, you have to call as_view() function so as to return a 
callable view that takes a request and returns a response. 
Its the main entry-point in request-response cycle in case of generic views.

as_view is the function(class method) which will connect my MyView class with its url.'''