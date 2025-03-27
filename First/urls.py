from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),          # Task list view
    path('create/', views.task_create, name='task_create'),  # Create task view
    path('update/', views.task_update, name='task_update'),  # Update task view
    path('delete/', views.task_delete, name='task_delete'),  # Delete task view
]

