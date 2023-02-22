from django.urls import path
from . import views

urlpatterns = [
    path("",views.home , name="index"),
    #from tasks 
    path("sign_up/", views.signup ,name= "registrarse"),
    path("tasks/", views.tasks, name= 'tareas'  ),
    path("tasks_completed/ ", views.completed ,name= 'completed'),
    path( 'log_out/', views.log_out ,name= 'logout'),
    path( 'sign_in/', views.signin ,name= 'signin'),
    path( 'tasks/create_task/', views.createtasks ,name= 'tasks maker' ),
    path( 'tasks/<int:task_id>/', views.task_detail , name='taskdetail'),
    path( 'tasks/<int:id>/complete/', views.task_complete , name='task_completed'),
    path( 'tasks/<int:id>/delete/', views.task_delete , name='deletetask'),
]