from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def index(request):
    return HttpResponse("Welcome to Barberplace Appointments!")

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments:index')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create_appointment.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all().order_by('-date', '-time')
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments:appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/edit_appointment.html', {'form': form, 'appointment': appointment})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointments:appointment_list')
    return render(request, 'appointments/delete_appointment.html', {'appointment': appointment})

def available_appointments(request):
    available = Appointment.objects.filter(status='scheduled').order_by('date', 'time')
    return render(request, 'appointments/available_appointments.html', {'available': available})

@login_required
def client_appointments(request):
    appointments = Appointment.objects.filter(client=request.user.client)
    return render(request, 'appointments/client_appointments.html', {'appointments': appointments})
