from django.urls import path
from .views import todo_list, todo_delete

urlpatterns = [
    path('todos/', todo_list),
    path('todos/<int:pk>/', todo_delete),
]
