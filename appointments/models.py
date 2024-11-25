from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField()  # Тривалість послуги

    def __str__(self):
        return self.name
class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=[
        ('scheduled', 'Заплановано'),
        ('completed', 'Виконано'),
        ('canceled', 'Скасовано'),
    ])

    def __str__(self):
        return f"{self.client} - {self.service} on {self.date} at {self.time}"
