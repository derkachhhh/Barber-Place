from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_appointment, name='create_appointment'),
    path('list/', views.appointment_list, name='appointment_list'),
    path('edit/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('available/', views.available_appointments, name='available_appointments'),
    path('my-appointments/', views.client_appointments, name='client_appointments'),  # Записи клієнта
]

