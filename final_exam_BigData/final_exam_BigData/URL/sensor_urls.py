from django.urls import path
from . import views

urlpatterns = [
    path('', views.sensor_list, name='sensor_list'),
    path('<int:pk>/', views.sensor_detail, name='sensor_detail'),
    path('create/', views.sensor_create, name='sensor_create'),
    path('<int:pk>/edit/', views.sensor_update, name='sensor_update'),
    path('<int:pk>/delete/', views.sensor_delete, name='sensor_delete'),
]
