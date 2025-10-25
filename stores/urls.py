from django.urls import path
from . import views




urlpatterns = [
    path('', views.stores, name='stores'),
    # 127.0.0.1/stores             list all stores
    path('details/<int:id>', views.details, name='store_details'),
    # 127.0.0.1/stores/details/1    show the store#1
    path('bookings/', views.my_bookings, name='my_bookings'),
    # 127.0.0.1/stores/bookings     show the bookings of the logined user
    path('booking/<int:store_id>/', views.booking, name='booking'),
    # 127.0.0.1/stores/booking/1    booking the store#1
    
]
    
