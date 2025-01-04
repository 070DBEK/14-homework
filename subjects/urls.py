from django.urls import path
from . import views


app_name = 'subjects'


urlpatterns = [
    path('list/', views.subject_list, name='list'),
    path('add/', views.create_subject, name='create'),
    path('delete/<int:pk>/', views.subject_delete, name='delete'),
    path('update/<int:subject_id>/', views.update_subject, name='update'),
    path('detail/<int:pk>/', views.subject_detail, name='detail'),
]