from traceback import print_tb
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from linebot import LineBotApi
from linebot.models import *
from .forms import RemindersForms, RemindersDrugForms
from .models import Reminders, RemindersDrug, TimeDrug
line_bot_api = LineBotApi(
    'Hk+4eFuOHBD7EN38YB5FvmlpGvgL7SAa2QWV50gvuUZ4JOeiUqfKMweft3wF1Sv6ilyqmPM+JqsHFWlBVkI9uUItXjxtwc5e1K0hhyp3mqgOwXHJ4ecLGigMwoHuME8HLOr0LNWHx9FhnRhiGubIxAdB04t89/1O/w1cDnyilFU=')
# Create your views here.


def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')


def liff(request):
    return render(request, 'liff.html')

def st5(request):
    if request.method == 'GET':
        return render(request, 'st5.html')
    else:
        id = request.POST['userId']
        q1 = int(request.POST['q1'])
        q2 = int(request.POST['q2'])
        q3 = int(request.POST['q3'])
        q4 = int(request.POST['q4'])
        q5 = int(request.POST['q5'])
        sum = q1 + q2 + q3 + q4 + q5
        if sum <= 4:
            text_message = TextSendMessage(text='ระดับความเครียด : เล็กน้อย')
            text_message2 = TextSendMessage(
                text='แนวทางการดูแล : เป็นความเครียดที่เกิดขึ้นได้ในชีวิตประจำวันและสามารถปรับตัวกับสถานการณ์ต่างๆ ได้อย่างเหมาะสม')
            line_bot_api.push_message(id, [text_message, text_message2])
        elif sum > 4 and sum <= 7:
            text_message = TextSendMessage(text='ระดับความเครียด : ปานกลาง')
            text_message2 = TextSendMessage(
                text='แนวทางการดูแล : สามารถผ่อนคลายความเครียดด้วยการทำกิจกรรมที่เพิ่มพลังเช่น ออกกำลังกาย เล่นกีฬาทำสิ่งที่สนุกสนานเพลิดเพลิน เช่นอ่านหนังสือ ฟังเพลง ทำงานอดิเรก หรือ พูดคุยระบายความไม่สบายใจกับผู้ที่ไว้วางใจ')
            line_bot_api.push_message(id, [text_message, text_message2])
        elif sum > 7 and sum <= 9:
            text_message = TextSendMessage(text='ระดับความเครียด : มาก')
            text_message2 = TextSendMessage(text='แนวทางการดูแล : การฝึกหายใจคลายเครียด พูดคุยระบายความเครียดกับผู้ที่ไว้วางใจ หาสาเหตุหรือปัญหาที่ทำให้เกิดความเครียดและหาวิธีแก้ไข หากท่านไม่สามารถจัดการคลายเครียดด้วยตนเอง ควรปรึกษากับผู้ให้การปรึกษาในหน่วยงานต่างๆ เช่น หน่วยบริการให้การปรึกษา / คลายเครียด\n- โรงพยาบาลจิตเวชขอนแก่นราชนครินทร์\n- ความรู้สุขภาพจิต 1667, สายด่วน / Hot line 1323')
            line_bot_api.push_message(id, [text_message, text_message2])
        elif sum > 9:
            text_message = TextSendMessage(text='ระดับความเครียด : มากที่สุด')
            text_message2 = TextSendMessage(text='ควรได้รับการช่วยเหลือจากผู้ให้การปรึกษาอย่างรวดเร็ว เช่น ทางโทรศัพท์ หรือ ผู้ให้การปรึกษาในหน่วยงานต่างๆ การเข้าถึงบริการ แหล่งความช่วยเหลือมีดังนี้ หน่วยบริการให้การปรึกษา / คลายเครียด\n- โรงพยาบาลจิตเวชขอนแก่นราชนครินทร์\n- ความรู้สุขภาพจิต 1667, สายด่วน / Hot line 1323\n- ควรได้รับการช่วยเหลือจากผู้ให้การปรึกษาอย่างรวดเร็ว เช่น ทางโทรศัพท์ หรือ ผู้ให้การปรึกษาในหน่วยงานต่างๆ การเข้าถึงบริการ แหล่งความช่วยเหลือมีดังนี้')
            line_bot_api.push_message(id, [text_message, text_message2])
        return render(request, 'close.html')


def q8(request):
    if request.method == 'GET':
        return render(request, 'q8.html')
    else:
        id = request.POST['userId']
        q1 = int(request.POST['q1'])
        q2 = int(request.POST['q2'])
        q3 = int(request.POST['q3'])
        try:
            q3q = int(request.POST['q3q'])
        except:
            q3q = 0
        q4 = int(request.POST['q4'])
        q5 = int(request.POST['q5'])
        q6 = int(request.POST['q6'])
        q7 = int(request.POST['q7'])
        q8 = int(request.POST['q8'])
        sum = q1 + q2 + q3 + q3q + q4 + q5 + q6 + q7 + q8
        print(sum)
        if sum == 0:
            line_bot_api.push_message(id, TextSendMessage(
                text='ไม่มีแนวโน้มฆ่าตัวตายในปัจจุบัน'))
        elif sum >= 1 and sum <= 8:
            text_message = TextSendMessage(text='มีแนวโน้มทำร้ายตัวเอง เล็กน้อย')
            text_message2 = TextSendMessage(
                text='แนวทางการดูแล : ควรปรึกษาหรือส่งต่อผู้ชำนาญด้านให้การปรึกษาหรือผู้ทำงานด้านสุขภาพจิตที่ได้รับการฝึกอบรมมาดีแล้วเพื่อให้การช่วยเหลือทางสังคมจิตใจ')
            line_bot_api.push_message(id, [text_message, text_message2])
        elif sum >= 9 and sum <= 16:
            text_message = TextSendMessage(text='มีแนวโน้มทำร้ายตัวเอง ปานกลาง')
            text_message2 = TextSendMessage(
                text='แนวทางการดูแล : ควรมีญาติดูแลอย่างใกล้ชิด และให้พามาพบแพทย์ทันที')
            line_bot_api.push_message(id, [text_message, text_message2])
        elif sum >= 17:
            text_message = TextSendMessage(text='มีแนวโน้มทำร้ายตัวเอง รุนแรง')
            text_message2 = TextSendMessage(
                text='แนวทางการดูแล : ควรมีญาติดูแลอย่างใกล้ชิด และให้พามาพบแพทย์ทันที')
            line_bot_api.push_message(id, [text_message, text_message2])
        return render(request, 'close.html')


def q9(request):
    if request.method == 'GET':
        return render(request, 'q9.html')
    else:
        id = request.POST['userId']
        q1 = int(request.POST['q1'])
        q2 = int(request.POST['q2'])
        q3 = int(request.POST['q3'])
        q4 = int(request.POST['q4'])
        q5 = int(request.POST['q5'])
        q6 = int(request.POST['q6'])
        q7 = int(request.POST['q7'])
        q8 = int(request.POST['q8'])
        q9 = int(request.POST['q9'])
        sum = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9
        if sum < 7:
            text_message = TextSendMessage(text='ไม่มีภาวะซึมเศร้า')
            line_bot_api.push_message(id, text_message)
        elif sum >= 7 and sum <= 12:
            text_message = TextSendMessage(text='มีแนวโน้มจะเป็นโรคซึมเศร้าระดับน้อย')
            text_message2 = TextSendMessage(
                text='แนวทางการดูแล : แนะนำวิธีการคลายเครียดด้วยตนเอง เช่น การพูดคุยระบายความรู้สึก การนวด การฟังเพลง การทำสมาธิ การผ่อนคลายกล้ามเนื้อ')
            line_bot_api.push_message(id, [text_message, text_message2])
        elif sum >= 13 and sum <= 18:
            text_message = TextSendMessage(text='มีแนวโน้มจะเป็นโรคซึมเศร้าระดับปานกลาง')
            text_message2 = TextSendMessage(
                text='แนวทางการดูแล : แนะนำวิธีการคลายเครียดด้วยตนเอง เช่น การพูดคุยระบายความรู้สึก การนวด การฟังเพลง การทำสมาธิ การผ่อนคลายกล้ามเนื้อ\n- หากไม่ดีขึ้นให้ ให้พามาพบแพทย์ทันที')
            line_bot_api.push_message(id, [text_message, text_message2])
        elif sum >= 19:
            text_message = TextSendMessage(text='มีแนวโน้มจะเป็นโรคซึมเศร้ารุนแรง')
            text_message2 = TextSendMessage(
                text='แนวทางการดูแล : แนะนำวิธีการคลายเครียดด้วยตนเอง เช่น การพูดคุยระบายความรู้สึก การนวด การฟังเพลง การทำสมาธิ การผ่อนคลายกล้ามเนื้อ\n- หากมีความเสี่ยงต่อการฆ่าตัวตาย ควรมีญาติดูแลอย่างใกล้ชิด และให้พามาพบแพทย์ทันที')
            line_bot_api.push_message(id, [text_message, text_message2])
        return render(request, 'close.html')


def reminder(request, userid=None):
    if request.method == 'GET':
        try:
            reminders = Reminders.objects.filter(user_id=userid)
        except:
            reminders = None
        return render(request, 'reminder_index.html', {'reminders': reminders, 'userid': userid})
     
def reminder_add(request, userid=None):
    if request.method == 'GET':
        form = RemindersForms(initial={'user_id': userid})
        return render(request, 'reminder.html', {'form': form, 'id':None})
    else:
        form = RemindersForms(request.POST)
        userid = request.POST.get('user_id')
        if form.is_valid():
            form.save()

        return redirect('reminder', userid=userid)

def reminder_edit(request, id=None):
    reminders = Reminders.objects.get(id=id)
    if request.method == 'GET':
        form = RemindersForms(instance=reminders)
        return render(request, 'reminder.html', {'form': form, 'id':id})
    else:
        form = RemindersForms(request.POST, instance=reminders)
        userid = request.POST.get('user_id')
        if form.is_valid():
            form.save()

        return redirect('reminder', userid=userid)


def reminder_delete(request, userid=None, id=None):
    reminders = Reminders.objects.get(id=id)
    reminders.delete()
    return redirect('reminder', userid=userid)


def reminderdrug(request, userid=None):
    if request.method == 'GET':
        try:
            reminders = RemindersDrug.objects.get(user_id=userid)
        except:
            reminders = None
        if reminders != None:
            form = RemindersDrugForms(instance=reminders)
            return render(request, 'reminder_drug.html', {'form': form})
        else:
            form = RemindersDrugForms(initial={'user_id': userid})
            return render(request, 'reminder_drug.html', {'form': form})
    else:
        userid = request.POST['user_id']
        try:
            reminders = RemindersDrug.objects.get(user_id=userid)
            form = RemindersDrugForms(request.POST, instance=reminders)
            if form.is_valid():
                form.save()
        except:
            form = RemindersDrugForms(request.POST)
            if form.is_valid():
                form.save()

        return render(request, 'close.html')


def update_something():
    now = datetime.today()
    print(now.strftime("%Y-%m-%d"))
    print(now.strftime("%H:%M:%S"))
    reminders = Reminders.objects.filter(date_user=now.strftime(
        "%Y-%m-%d"), time_user=now.strftime("%H:%M:%S"))
    text_ser = 'คุณมีแจ้งเตือน⏰\n'
    for a in reminders:
        reminders_user = a.reminders_user
        if reminders_user == '':
            reminders_user = '-'
        user_id = a.user_id
        date_user = a.date_user
        time_user = a.time_user
        s = a.service.all()
        if s.count() != 0:
            for i in s:
                text_ser = text_ser + '✅' + str(i) + '\n'
        else:
            text_ser = text_ser
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
        text_req = f'{text_ser}📌 หมายเหตุ : {reminders_user}\n📅 วันที่ : {date_user.strftime("%d")}-{m[str(date_user.strftime("%m"))]}-{int(date_user.strftime("%Y"))+543}\n🕓 เวลา : {time_user}'
        text_message = TextSendMessage(text=text_req)
        line_bot_api.push_message(user_id, text_message)
        text_ser = 'คุณมีแจ้งเตือน⏰\n'


def update_something_next_day():
    now = datetime.today()
    next_day = now + timedelta(days=1)
    reminders = Reminders.objects.filter(date_user=next_day.strftime(
        "%Y-%m-%d"), time_user=next_day.strftime("%H:%M:%S"))
    text_ser = 'คุณมีแจ้งเตือนล่วงหน้า⏰\n'
    for a in reminders:
        reminders_user = a.reminders_user
        if reminders_user == '':
            reminders_user = '-'
        user_id = a.user_id
        date_user = a.date_user
        time_user = a.time_user
        s = a.service.all()
        if s.count() != 0:
            for i in s:
                text_ser = text_ser + '✅' + str(i) + '\n'
        else:
            text_ser = text_ser
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
        text_req = f'{text_ser}📌 หมายเหตุ : {reminders_user}\n📅 วันที่ : {date_user.strftime("%d")}-{m[str(date_user.strftime("%m"))]}-{int(date_user.strftime("%Y"))+543}\n🕓 เวลา : {time_user} \n อย่าลืมนะคะ 😊'
        text_message = TextSendMessage(text=text_req)
        line_bot_api.push_message(user_id, text_message)
        text_ser = 'คุณมีแจ้งเตือนล่วงหน้า⏰\n'

def update_drug():
    # now = datetime.today()
    # reminders = RemindersDrug.objects.all()
    # for a in reminders:
    #     user_id = a.user_id
    #     s = a.time_drug.all()
    #     if s.count() != 0:
    #         for i in s:
    #             print(user_id)
    #             print(i.time_drug)

    # reminders = TimeDrug.objects.filter(time_drug='12:00:00')
    # print(reminders)

    now = datetime.today()

    reminders = RemindersDrug.objects.filter(time_drug__time_drug__startswith=now.strftime("%H:%M:%S"))
    print(reminders)
    text_ser = 'คุณมีแจ้งเตือนกินยา💊⏰\n'
    for a in reminders:
        user_id = a.user_id
        reminders_user = a.reminders_user
        if reminders_user == '':
            reminders_user = '-'
        s = a.time_drug.filter(time_drug=now.strftime("%H:%M:%S"))

        for i in s:
            text_ser = text_ser + '✅' + str(i) + '\n'

        text_req = f'{text_ser} หมายเหตุ : {reminders_user}'
        text_message = TextSendMessage(text=text_req)
        line_bot_api.push_message(user_id, text_message)
        text_ser = 'คุณมีแจ้งเตือนกินยา💊⏰\n'

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=update_something, trigger='cron', minute='*')
    scheduler.start()

    scheduler2 = BackgroundScheduler()
    scheduler2.add_job(func=update_something_next_day,
                       trigger='cron', minute='*')
    scheduler2.start()

    scheduler3 = BackgroundScheduler()
    scheduler3.add_job(func=update_drug,
                       trigger='cron', minute='*')
    scheduler3.start()

    # scheduler3 = BackgroundScheduler()
    # scheduler3.add_job(func=update_drug,
    #                    trigger='cron', hour='13', minute='10')
    # scheduler3.start()

# python manage.py runserver --noreload
