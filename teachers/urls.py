from django.urls import path
from . import views


app_name = 'teachers'


urlpatterns = [
    path('list/', views.teachers_list, name='list'),
    path('create/', views.create_teacher, name='create'),
    path('delete/<int:pk>/', views.teacher_delete, name='delete'),
    path('update/<int:pk>/', views.update_teacher, name='update'),
    path('detail/<int:pk>/', views.teacher_detail, name='detail'),
]