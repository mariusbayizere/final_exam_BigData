from django.urls import path
from . import views

urlpatterns = [
    path('', views.sensor_data_list, name='sensor_data_list'),
    path('<int:pk>/', views.sensor_data_detail, name='sensor_data_detail'),
    path('create/', views.sensor_data_create, name='sensor_data_create'),
    path('<int:pk>/edit/', views.sensor_data_update, name='sensor_data_update'),
    path('<int:pk>/delete/', views.sensor_data_delete, name='sensor_data_delete'),
]
