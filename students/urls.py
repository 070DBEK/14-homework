from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'students'


urlpatterns = [
    path('list/', views.students_list, name='list'),
    path('add/', views.create_student, name='create'),
    path('edit/<int:student_id>/', views.create_student, name='edit'),
    path('detail/<int:student_id>/', views.student_detail, name='detail'),
    path('delete/<int:student_id>/', views.student_delete, name='delete'),
]

