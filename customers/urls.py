from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('customers/', views.customers, name='customers'),
    path('customers/details/<int:id>', views.details, name='details'),
    path('toast_detail/', views.toast_de, name='toast_de'),
    path('ingredient_detail/', views.ingredient_de, name='ingredient_de'),
    
]