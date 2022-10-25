from django.db import models
from datetime import datetime

# Create your models here.
class Service(models.Model):
    name_service = models.CharField(max_length=255)

    def __str__(self):
        return self.name_service

class Reminders(models.Model):
    user_id = models.CharField(max_length=255)
    service =  models.ManyToManyField(Service, blank=True)
    reminders_user = models.TextField(blank=True)
    date_user = models.DateField(blank=False)
    time_user = models.TimeField(blank=False)

    def __str__(self):
        return self.user_id



class TimeDrug(models.Model):
    time_drug = models.TimeField(blank=False)
    text_drug = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.time_drug.strftime("%H:%M")} : {self.text_drug}'


class RemindersDrug(models.Model):
    user_id = models.CharField(max_length=255)
    time_drug =  models.ManyToManyField(TimeDrug, blank=True)
    reminders_user = models.TextField(blank=True)

    def __str__(self):
        return self.user_id
