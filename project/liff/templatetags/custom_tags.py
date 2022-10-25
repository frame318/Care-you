from django import template
import datetime

register = template.Library()

m = {
            '01': 'มกราคม',
            '02': 'กุมภาพันธ์',
            '03': 'มีนาคม',
            '04': 'เมษายน',
            '05': 'พฤษภาคม',
            '06': 'มิถุนายน',
            '07': 'กรกฎาคม',
            '08': 'สิงหาคม',
            '09': 'กันยายน',
            '10': 'ตุลาคม',
            '11': 'พฤศจิกายน',
            '12': 'ธันวาคม',
        }

@register.filter(name='format_date')
def format_date(date_string):
    return f'{date_string.strftime("%d")} {m[str(date_string.strftime("%m"))]} {int(date_string.strftime("%Y"))+543}'

@register.filter(name='format_time')
def format_time(time_string):
    return f'{time_string.strftime("%H:%M")}'