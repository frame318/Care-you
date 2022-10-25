from django import forms
from .models import *
from django.template.defaultfilters import mark_safe

class RemindersForms(forms.ModelForm):
    service = forms.ModelMultipleChoiceField(
            queryset=Service.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            label= mark_safe('<strong>✅ บริการ</strong>'),
            required=False)
    class Meta:
         model = Reminders
         fields = '__all__'
         widgets = {
                'user_id': forms.HiddenInput(),
                'reminders_user': forms.Textarea(attrs={'rows': 4}),
                'date_user': forms.DateInput(attrs={'type':'date'}),
                'time_user': forms.TimeInput(format='%H:%M:%S',attrs={'type':'time'}),
                }
         labels = {
                'reminders_user': mark_safe('<strong>📌 หมายเหตุอื่นๆ</strong>'),
                'date_user': mark_safe('<strong>📅 วันที่</strong>'),
                'time_user': mark_safe('<strong>🕓 เวลา</strong>'),
            }

class RemindersDrugForms(forms.ModelForm):
    time_drug = forms.ModelMultipleChoiceField(
            queryset=TimeDrug.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            label=mark_safe('<strong>เวลา</strong>'),
            required=False)
    class Meta:
        model = RemindersDrug
        fields = '__all__'
        widgets = {
               'user_id': forms.HiddenInput(),
               'reminders_user': forms.Textarea(attrs={'rows': 4}),
                }
        labels = {
               'reminders_user': mark_safe('<strong>หมายเหตุอื่นๆ</strong>'),
               # 'reminders_user': 'หมายเหตุอื่นๆ',

           }
