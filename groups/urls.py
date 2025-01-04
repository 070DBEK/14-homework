from django.urls import path
from . import views


app_name = 'groups'


urlpatterns = [
    path('list/', views.groups_list, name='list'),
    path('add/', views.create_group, name='create'),
    path('detail/<int:group_id>/', views.group_detail, name='detail'),
    path('delete/<int:pk>/', views.group_delete, name='delete')
]