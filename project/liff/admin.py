from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Service)
admin.site.register(Reminders)

admin.site.register(TimeDrug)
admin.site.register(RemindersDrug)
