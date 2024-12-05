from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_training_list, name='model_training_list'),
    path('<int:pk>/', views.model_training_detail, name='model_training_detail'),
    path('create/', views.model_training_create, name='model_training_create'),
    path('<int:pk>/edit/', views.model_training_update, name='model_training_update'),
    path('<int:pk>/delete/', views.model_training_delete, name='model_training_delete'),
]
