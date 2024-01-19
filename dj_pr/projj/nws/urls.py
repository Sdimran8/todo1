from django.urls import path
from .import views
urlpatterns = [
    path('',views.SignUp,name='signup'),
    path('login',views.LogIn,name='login'),
    path('logout',views.LogOut,name='logout'),
    path('delete/<int:user_id>',views.Delete,name='delete'),
    path('home/<int:user_id>',views.Home,name='home'),   
    path('',views.todo_list,name="todo_list"),
    path('create',views.create_todo,name="create_todo"),
    path('complete/<int:todo_id>',views.complete_todo,name="complete_todo"),
    path('delete/<int:todo_id>',views.delete_todo,name="delete_todo"),   
]