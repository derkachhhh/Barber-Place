
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings
from .models import Appointment

def send_reminders():
    # Отримати записи, заплановані на наступний день
    tomorrow = datetime.now().date() + timedelta(days=1)
    appointments = Appointment.objects.filter(date=tomorrow, status='scheduled')

    for appointment in appointments:
        subject = "Нагадування про запис"
        message = f"Шановний(а) {appointment.client}, ви записані на {appointment.service} з {appointment.staff} " \
                  f"на {appointment.date} о {appointment.time}. Будемо раді вас бачити!"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [appointment.client.email])
