from django.urls import path
from . import views


app_name = 'subjects'


urlpatterns = [
    path('list/', views.subject_list, name='list'),
    path('create/', views.subject_create, name='create'),
    path('<int:pk>/', views.subject_detail, name='detail'),
    path('<int:pk>/update/', views.update_subject, name='update'),
    path('<int:pk>/delete/', views.subject_delete, name='delete'),
]
