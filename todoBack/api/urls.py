from django.urls import path
from api.views import views_old, fbv, cbv 

urlpatterns = [ 
    #path('task_lists/', fbv.task_lists),
    path('task_lists/', cbv.TaskListTasks.as_view()),
    #path('task_lists/<int:pk>/', fbv.task_list_detail),
    path('task_lists/<int:pk>/', cbv.TasksList.as_view()),
    path('task_lists/<int:pk>/tasks/', fbv.task_list_tasks),
    path('tasks/<int:pk>/', fbv.task_detail)
]