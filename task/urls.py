from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.tasks, name='tasks'),
    path('task/<int:pk>/', views.task, name='task'),
    path('create-task/', views.create_task, name='create-task'),
    path('edit-task/<int:pk>/', views.edit_task, name='edit-task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete-task'),
    path('delete-tasks/', views.delete_tasks, name='delete-tasks'),
    path('delete-complete-tasks/', views.delete_complete_tasks, name='delete-complete-tasks'),
]
