
from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview , name='api-overview'),
    path('task-list/' , views.taskOverview, name= "task-list"),
    path('detail-task/<str:pk>' , views.taskDetail, name= "detail-task"),
    path('task-create/', views.createTask,  name="task-create"),
    path('update-task/<str:pk>', views.updateTask , name="update-task"),
    path('delete-task/<str:pk>', views.deleteTask , name="delete-task")
]
