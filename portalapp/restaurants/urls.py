from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/new/', views.restaurant_create, name='restaurant_create'),
    path('restaurant/<int:pk>/update/', views.restaurant_update, name='restaurant_update'),
    path('restaurant/<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),
]
