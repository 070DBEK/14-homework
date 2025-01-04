from django.urls import path
from . import views


app_name = 'students'


urlpatterns = [
    path('list/', views.students_list, name='list'),
    path('add/', views.create_student, name='create'),
    path('detail/<int:pk>', views.student_detail, name='detail'),
    path('delete/<int:pk>', views.student_delete , name='delete'),
]