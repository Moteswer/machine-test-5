# flywithme/urls.py
from django.urls import path
from .views import flight_list, flight_detail, flight_add, flight_edit, login_view, logout_view

urlpatterns = [
    path('flight/', flight_add, name='add_flight'),  # Set default page to 'flight_add'
    path('flights/', flight_list, name='flight_list'),
    path('flights/<int:flight_id>/', flight_detail, name='flight_detail'),
    path('flights/add/', flight_add, name='flight_add'),
    path('flights/edit/<int:flight_id>/', flight_edit, name='flight_edit'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
