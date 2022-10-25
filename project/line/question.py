from django.shortcuts import render
from django.db.models import F, Func, Value, CharField
from linebot import LineBotApi
from linebot.models import *
from liff.models import *
import requests
import json

line_bot_api = LineBotApi('Hk+4eFuOHBD7EN38YB5FvmlpGvgL7SAa2QWV50gvuUZ4JOeiUqfKMweft3wF1Sv6ilyqmPM+JqsHFWlBVkI9uUItXjxtwc5e1K0hhyp3mqgOwXHJ4ecLGigMwoHuME8HLOr0LNWHx9FhnRhiGubIxAdB04t89/1O/w1cDnyilFU=')

class Question:
    pass
    def __init__(self, replytoken, intent, text, userid, body):
        self.replytoken = replytoken
        self.intent = intent
        self.text = text
        self.userid = userid
        self.body = body
    def question(self):
        if self.text == 'สอบถามปัญหาอีกครั้ง':
            text_message = TextSendMessage(text='สอบถามได้เลยคะ')
            line_bot_api.reply_message(self.replytoken , text_message)
            line_bot_api.link_rich_menu_to_user(self.userid, 'richmenu-d115e26182c89b25468c6882416fd139')
        else:
            text_message = TextSendMessage(text='สวัสดี')
            text_message2 = TextSendMessage(
                text='care you  เป็นหุ่นยนต์ถามตอบเกี่ยวกับให้บริการ เรื่องการเลื่อนนัด คำแนะนำทั่วไปสำหรับผู้ป่วย และ ผู้ดูแล ที่ได้มารับบริการโรงพยาบาลจิตเวชขอนแก่นราชนครินทร์ ')
            flex_message = FlexSendMessage(
                alt_text='hello',
                contents={
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "การเลื่อนนัด",
                                    "text": "การเลื่อนนัด"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "การกินยา",
                                    "text": "การกินยา"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "คลินิกนอกเวลา",
                                    "text": "คลินิกนอกเวลา"
                                }
                            },
                            # {
                            #     "type": "button",
                            #     "style": "secondary",
                            #     "action": {
                            #         "type": "message",
                            #         "label": "Covid 19",
                            #         "text": "Covid 19"
                            #     }
                            # },

                        ]
                    }
                }
            )
            line_bot_api.reply_message(self.replytoken, [text_message, text_message2, flex_message])
            line_bot_api.link_rich_menu_to_user(self.userid, 'richmenu-d115e26182c89b25468c6882416fd139')
    def questionfallback(self):
        text_message = TextSendMessage(text='โทษค่ะเรายังไม่เข้าใจลองถามใหม่อีกครั้ง หรือเลือกเมนูข้างล่าง นะคะ',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="การเลื่อนนัด", text="การเลื่อนนัด")),
                                   QuickReplyButton(action=MessageAction(label="การกินยา", text="การกินยา")),
                                   QuickReplyButton(action=MessageAction(label="คลินิกนอกเวลา", text="คลินิกนอกเวลา")),

                               ]))
        line_bot_api.reply_message(self.replytoken, text_message)
    def menu(self):
        if self.intent == 'Menu':
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='ต้องการหยุดการสนทนา',
                    actions=[
                        MessageAction(
                            label='ใช่',
                            text='ใช่'
                        ),
                        MessageAction(
                            label='ไม่ใช่',
                            text='สอบถามปัญหาอีกครั้ง'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, confirm_template_message)
        if self.intent == 'Menu - yes':
            line_bot_api.unlink_rich_menu_from_user(self.userid)
    def reply(self):
        if self.intent == 'Question - sticker':
            text_message = TextSendMessage(text='ก่อนจะคุยกันเรามาวัดอุณหภูมิใจกันไหมคะ')
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='วัดอุณหภูมิใจ',
                    actions=[
                        MessageAction(
                            label='ทำ',
                            text='ทำ'
                        ),
                        MessageAction(
                            label='ไม่ทำ',
                            text='สอบถามปัญหาอีกครั้ง'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, [text_message, confirm_template_message])
        if self.intent == 'Question - sticker - yes':
            imagemap_message = ImagemapSendMessage(
                base_url='https://sv1.picz.in.th/images/2020/10/26/bTUnYl.jpg',
                alt_text='this is an imagemap',
                base_size=BaseSize(height=600, width=1040),
                actions=[
                     MessageImagemapAction(
                            text='1',
                            area=ImagemapArea(
                            x=125, y=169, width=154, height=187
                            )
                    ),
                     MessageImagemapAction(
                           text='2',
                           area=ImagemapArea(
                           x=292, y=166, width=138, height=190
                           )
                    ),
                     MessageImagemapAction(
                          text='3',
                          area=ImagemapArea(
                          x=449, y=164, width=153, height=196
                          )
                    ),
                      MessageImagemapAction(
                             text='4',
                             area=ImagemapArea(
                             x=612, y=164, width=137, height=195
                             )
                     ),
                      MessageImagemapAction(
                            text='5',
                            area=ImagemapArea(
                            x=767, y=167, width=144, height=194
                            )
                     ),
                      MessageImagemapAction(
                           text='6',
                           area=ImagemapArea(
                           x=111, y=372, width=146, height=210
                           )
                    ),
                      MessageImagemapAction(
                          text='7',
                          area=ImagemapArea(
                          x=273, y=375, width=148, height=208
                          )
                    ),
                      MessageImagemapAction(
                          text='8',
                          area=ImagemapArea(
                          x=439, y=367, width=148, height=214
                          )
                    ),
                      MessageImagemapAction(
                          text='9',
                          area=ImagemapArea(
                          x=603, y=375, width=151, height=208
                          )
                    ),
                      MessageImagemapAction(
                          text='10',
                          area=ImagemapArea(
                          x=776, y=374, width=146, height=209
                          )
                   ),
                ]
            )
            line_bot_api.reply_message(self.replytoken, imagemap_message)
        if self.intent == 'Question - sticker - yes - 1':
            num = int(self.body["queryResult"]["outputContexts"][0]["parameters"]['number.original'])
            if num >= 8:
                text_message = TextSendMessage(text='ระดับ 8-10 คะแนนดีมากคะ')
                flex_message = FlexSendMessage(
                    alt_text='hello',
                    contents={
                        "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "md",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "action": {
                                        "type": "message",
                                        "label": "การเลื่อนนัด",
                                        "text": "การเลื่อนนัด"
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "action": {
                                        "type": "message",
                                        "label": "การกินยา",
                                        "text": "การกินยา"
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "action": {
                                        "type": "message",
                                        "label": "คลินิกนอกเวลา",
                                        "text": "คลินิกนอกเวลา"
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "action": {
                                        "type": "message",
                                        "label": "อื่นๆ",
                                        "text": "อื่นๆ"
                                    }
                                },

                            ]
                        }
                    }
                )
                text_message2 = TextSendMessage(text='สอบถามอะไรคะ')
                line_bot_api.reply_message(self.replytoken, [text_message, text_message2, flex_message])
            if num >= 5 and num < 8:
                text_message = TextSendMessage(text='ระดับ 5-7 คะแนนใช้ได้คะ')
                text_message2 = TextSendMessage(
                    text='ถ้าคุณมีความเครียดแนะนำให้ฝึกสติ ตาม link ฝึกหายใจคลายเครียด กรมสุขภาพจิต https://www.youtube.com/watch?v=D-ozvjPlVy4 ')
                text_message3 = TextSendMessage(
                    text='เทคนิคการจัดการความเครียดด้วยตนเอง กรมสุขภาพจิต https://www.youtube.com/watch?v=kOLNFOKSDnk')
                line_bot_api.reply_message(self.replytoken, [text_message, text_message2, text_message3])
            if num < 5:
                text_message = TextSendMessage(text='ระดับ1-4 คะแนนไม่ค่อยดีคะ')
                text_message2 = TextSendMessage(
                    text='ถ้าไม่สบายใจแนะนำให้ปรึกษาเจ้าหน้าที่ รพ. ที่เบอร์ 043-237151 และ1323  ได้คะ')
                line_bot_api.reply_message(self.replytoken, [text_message, text_message2])
        if self.intent == 'Q1 - 1 - 1 - 1' or self.intent == 'Q1 - 1 - 1 - 2 - 1':
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='ยาพอกินไหม',
                    actions=[
                        MessageAction(
                            label='พอ',
                            text='พอ'
                        ),
                        MessageAction(
                            label='ไม่พอ',
                            text='ไม่พอ'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, confirm_template_message)
        if self.intent == 'Q1 - 1 - 1 - 1 - yes - 1' or self.intent == 'Q1 - 1 - 1 - 1 - no - 1' or self.intent == 'Q1 - 1 - 1 - 2 - 1 - yes - 1' or self.intent == 'Q1 - 1 - 1 - 2 - 1 - no - 1':
            text_message = TextSendMessage(text='จองคิวออนไลน์ได้ตาม link : http://122.154.130.61/que_online/')
            text_message2 = TextSendMessage(text='หรือโทรสอบถามข้อมูลที่ งานเวชระเบียน 043-209999 ต่อ 63101 ในเวลาราชการ ')
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='มีอะไรคุยอีกกันต่ออีกไหม ',
                    actions=[
                        MessageAction(
                            label='มี',
                            text='สอบถามปัญหาอีกครั้ง'
                        ),
                        MessageAction(
                            label='ไม่มี',
                            text='เมนูหลัก'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, [text_message, text_message2, confirm_template_message])
        if self.intent == 'Q1 - 2 - 1':
            text_message = TextSendMessage(text='ขออภัยค่ะ  อยากให้ลองโทรใหม่อีกครั้ง หรือ โทรไปที หมายเลข 1323')
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='มีอะไรคุยอีกกันต่ออีกไหม ',
                    actions=[
                        MessageAction(
                            label='มี',
                            text='สอบถามปัญหาอีกครั้ง'
                        ),
                        MessageAction(
                            label='ไม่มี',
                            text='เมนูหลัก'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, [text_message, confirm_template_message])
        if self.intent == 'Q2':
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='ตอนนี้ กินยาอยู่ไหม ',
                    actions=[
                        MessageAction(
                            label='กิน',
                            text='กิน'
                        ),
                        MessageAction(
                            label='ไม่กิน',
                            text='ไม่กิน'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, confirm_template_message)
        if self.intent == 'Q2 - yes - 2 - 1':
            text_message = TextSendMessage(text='ขออภัยค่ะ  อยากให้ลองโทรใหม่อีกครั้ง หรือ โทรไปที หมายเลข 1323')
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='มีอะไรคุยอีกกันต่ออีกไหม ',
                    actions=[
                        MessageAction(
                            label='มี',
                            text='สอบถามปัญหาอีกครั้ง'
                        ),
                        MessageAction(
                            label='ไม่มี',
                            text='เมนูหลัก'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, [text_message, confirm_template_message])
        if self.intent == 'Q2 - yes - 1 - 1':
            text_message = TextSendMessage(text='คราวหน้าที่มาพบหมอ ให้ถามหมอเรื่องการปรับยาด้วยนะคะ')
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='มีอะไรคุยอีกกันต่ออีกไหม ',
                    actions=[
                        MessageAction(
                            label='มี',
                            text='สอบถามปัญหาอีกครั้ง'
                        ),
                        MessageAction(
                            label='ไม่มี',
                            text='เมนูหลัก'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, [text_message, confirm_template_message])
        if self.intent == 'Q2 - no - 1 - 1':
            text_message = TextSendMessage(text='คราวหน้าที่มาพบหมอ ให้ถามหมอเรื่องการปรับยาด้วยนะคะ')
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='มีอะไรคุยอีกกันต่ออีกไหม ',
                    actions=[
                        MessageAction(
                            label='มี',
                            text='สอบถามปัญหาอีกครั้ง'
                        ),
                        MessageAction(
                            label='ไม่มี',
                            text='เมนูหลัก'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, [text_message, confirm_template_message])
        if self.intent == 'Q2 - no - 2 - 1':
            text_message = TextSendMessage(text='ขออภัยค่ะ  อยากให้ลองโทรใหม่อีกครั้ง หรือ โทรไปที หมายเลข 1323')
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='มีอะไรคุยอีกกันต่ออีกไหม ',
                    actions=[
                        MessageAction(
                            label='มี',
                            text='สอบถามปัญหาอีกครั้ง'
                        ),
                        MessageAction(
                            label='ไม่มี',
                            text='เมนูหลัก'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, [text_message, confirm_template_message])
        if self.intent == 'Q3 - 1':
            text_message = TextSendMessage(text='ลงทะเบียนในระบบออนไลน์ตาม QR cord นี้คะ')
            imagemap_message = ImagemapSendMessage(
                base_url='https://sv1.picz.in.th/images/2020/10/13/OIyiBJ.png',
                alt_text='this is an imagemap',
                base_size=BaseSize(height=966, width=1040),
                actions=[
                    URIImagemapAction(
                        link_uri='http://onelink.to/tf6v9h',
                        area=ImagemapArea(
                            x=27, y=20, width=990, height=946
                        )
                    ),
                ]
            )
            line_bot_api.reply_message(self.replytoken, [text_message, imagemap_message])
        if self.intent == 'test':
            data = requests.get('https://covid19.th-stat.com/api/open/today')
            json_data = json.loads(data.text)

            Confirmed = json_data['Confirmed']  # ติดเชื้อสะสม
            Recovered = json_data['Recovered']  # หายแล้ว
            Hospitalized = json_data['Hospitalized']  # รักษาอยู่ใน รพ.
            Deaths = json_data['Deaths']  # เสียชีวิต
            NewConfirmed = json_data['NewConfirmed']  # บวกเพิ่ม

            text_message = TextSendMessage(
                text='ติดเชื้อสะสม = {} คน(+เพิ่ม{})\nหายแล้ว = {} คน\nรักษาอยู่ใน รพ. = {} คน\nเสียชีวิต = {} คน'.format(
                    Confirmed, NewConfirmed, Recovered, Hospitalized, Deaths))
            line_bot_api.reply_message(self.replytoken, text_message)
    def reminder(self):
        if self.text == 'เตือนความจำ':
            buttons_template_message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1631176415/%E0%B9%80%E0%B8%95%E0%B8%B7%E0%B8%AD%E0%B8%99%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%88%E0%B8%B3/%E0%B9%80%E0%B8%95%E0%B8%B7%E0%B8%AD%E0%B8%99%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%88%E0%B8%B3_qpbhwm.jpg',
                    title='เตือนความจำ',
                    text='ช่วยสำหรับจดจำวันนัดหมาย',
                    actions=[
                        URIAction(
                            label='เตือนความจำ',
                            uri=f'https://liff.line.me/1654982439-PGQy8pvw/reminder/{self.userid}'
                        ),
                        MessageAction(
                            label='ดูบันทึกเตือนความจำ',
                            text='ดูบันทึกเตือนความจำ'
                        ),
                        URIAction(
                            label='เตือนการกินยา',
                            uri=f'https://liff.line.me/1654982439-PGQy8pvw/reminderdrug/{self.userid}'
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, buttons_template_message)
        if self.text == 'ดูบันทึกเตือนความจำ':
            text_ser = 'บันทึกเตือนความจำ⏰\n'
            reminders = Reminders.objects.filter(user_id = self.userid)
            if reminders.count() != 0:
                text = []
                for a in reminders:
                    reminders_user = a.reminders_user
                    if reminders_user == '':
                        reminders_user = '-'
                    date_user = a.date_user
                    time_user = a.time_user
                    s = a.service.all()
                    if s.count() != 0:
                        for i in s:
                            text_ser = text_ser + '✅' + str(i) + '\n'
                    else:
                        text_ser = text_ser
                    m = {
                        '01':'มกราคม',
                        '02':'กุมภาพันธ์',
                        '03':'มีนาคม',
                        '04':'เมษายน',
                        '05':'พฤษภาคม',
                        '06':'มิถุนายน',
                        '07':'กรกฎาคม',
                        '08':'สิงหาคม',
                        '09':'กันยายน',
                        '10':'ตุลาคม',
                        '11':'พฤศจิกายน',
                        '12':'ธันวาคม',
                        }
                    text_req = f'{text_ser}📌 หมายเหตุ : {reminders_user}\n📅 วันที่ : {date_user.strftime("%d")}-{m[str(date_user.strftime("%m"))]}-{int(date_user.strftime("%Y"))+543}\n🕓 เวลา : {time_user}'
                    text_message = TextSendMessage(text=text_req)
                    text.append(text_message)
                    text_ser = ''
                line_bot_api.reply_message(self.replytoken,text)
            else:
                text_message = TextSendMessage(text='คุณยังไม่มีบันทึกเตือนความจำ')
                line_bot_api.reply_message(self.replytoken, text_message)
    def drug(self):
        if self.text == 'รู้เรื่องยา':
            carousel_template_message = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630674655/%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A2%E0%B8%B2/%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%A2%E0%B8%B2%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%A7%E0%B8%8A_su1u3p.jpg',
                            title='ความรู้เกี่ยวกับยาจิตเวช',
                            text='สาระน่ารู้ควรรู้เกี่ยวกับยาจิตเวช',
                            actions=[
                                URIAction(
                                    label='ข้อควรรู้เกี่ยวกับยาจิตเวช',
                                    uri='https://www.manarom.com/blog/psychiatric_medications.html'
                                ),
                                MessageAction(
                                    label='วิดิโอน่ารู้เกี่ยวกับยาจิตเวช',
                                    text='วิดิโอน่ารู้เกี่ยวกับยาจิตเวช'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630674707/%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A2%E0%B8%B2/RDU_%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A2%E0%B8%B2_xwyoke.jpg',
                            title='RDU รู้เรื่องยา',
                            text='แอปพลิเคชันสำหรับใช้ดูข้อมูลฉลากยาเสริม',
                            actions=[
                                URIAction(
                                    label='IOS',
                                    uri='https://apps.apple.com/th/app/rdu-%E0%B8%A3-%E0%B9%80%E0%B8%A3-%E0%B8%AD%E0%B8%87%E0%B8%A2%E0%B8%B2/id1286704705?l=th'
                                ),
                                URIAction(
                                    label='Android',
                                    uri='https://play.google.com/store/apps/details?id=com.uhosnet&hl=th'
                                )
                            ]
                        )
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, carousel_template_message)
        if self.text == 'วิดิโอน่ารู้เกี่ยวกับยาจิตเวช':
            carousel_template_message = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630674950/%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A2%E0%B8%B2/%E0%B8%97%E0%B8%B3%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B9%80%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B9%83%E0%B8%88_%E0%B8%A2%E0%B8%B2%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%A7%E0%B8%8A_mdjxz7.png',
                            title='ทำความเข้าใจ "ยาจิตเวช"',
                            text='ปัญหาการใช้ ผลข้างเคียง',
                            actions=[
                                MessageAction(
                                    label='ดูวิดิโอ',
                                    text='วิดิโอน่ารู้เกี่ยวกับยาจิตเวช-1'
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630674997/%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A2%E0%B8%B2/%E0%B8%84%E0%B8%B3%E0%B8%96%E0%B8%B2%E0%B8%A1%E0%B8%A2%E0%B8%AD%E0%B8%94%E0%B8%AE%E0%B8%B4%E0%B8%95%E0%B8%A2%E0%B8%B2%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%A7%E0%B8%8A_avpzus.png',
                            title='คำถามยอดฮิตยาจิตเวช',
                            text='คำถามยอดฮิตยาจิตเวช',
                            actions=[
                                MessageAction(
                                    label='ดูวิดิโอ',
                                    text='วิดิโอน่ารู้เกี่ยวกับยาจิตเวช-2'
                                ),
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630675043/%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A2%E0%B8%B2/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%9B%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B8%94%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%A7%E0%B8%8A_oabccd.png',
                            title='การใช้ยากับผู้ป่วยด้านจิตเวช',
                            text='การใช้ยากับผู้ป่วยด้านจิตเวช',
                            actions=[
                                MessageAction(
                                    label='ดูวิดิโอ',
                                    text='วิดิโอน่ารู้เกี่ยวกับยาจิตเวช-3'
                                ),
                            ]
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, carousel_template_message)
        if self.text == 'วิดิโอน่ารู้เกี่ยวกับยาจิตเวช-1':
            text_message = TextSendMessage(text='https://www.youtube.com/watch?v=gQ5uqTLTtjY')
            line_bot_api.reply_message(self.replytoken, text_message)
        if self.text == 'วิดิโอน่ารู้เกี่ยวกับยาจิตเวช-2':
            text_message = TextSendMessage(text='https://www.youtube.com/watch?v=S9uO_ABmkU8')
            line_bot_api.reply_message(self.replytoken, text_message)
        if self.text == 'วิดิโอน่ารู้เกี่ยวกับยาจิตเวช-3':
            text_message = TextSendMessage(text='https://www.youtube.com/watch?v=bFBUmYF193E')
            line_bot_api.reply_message(self.replytoken, text_message)
    def knowledge(self):
        if self.text == 'เกร็ดความรู้':
            buttons_template_message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630599157/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/OIywF1_oodupb.png',
                    title='เกร็ดความรู้',
                    text='สาระน่ารู้',
                    actions=[
                        MessageAction(
                            label='การดูแลผู้ป่วยจิตเวช',
                            text='การดูแลผู้ป่วยจิตเวช'
                        ),
                        MessageAction(
                            label='การดูแลผู้ป่วยซึมเศร้า',
                            text='การดูแลผู้ป่วยซึมเศร้า'
                        ),
                        MessageAction(
                            label='การจัดการความเครียด',
                            text='การจัดการความเครียด'
                        ),
                        MessageAction(
                            label='เฝ้าระวังความเสี่ยง',
                            text='การเฝ้าระวังความเสี่ยงฆ่าตัวตาย'
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, buttons_template_message)
        if self.text == 'การดูแลผู้ป่วยจิตเวช':
            flex_message = FlexSendMessage(
                alt_text='hello',
                contents={
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "7 สัญญาณเตือน ผู้ป่วยจิตเวชยา",
                                    "text": "7 สัญญาณเตือน ผู้ป่วยจิตเวชยาเสพติดก่อความรุนแรง"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "โรคจิตเภท",
                                    "text": "โรคจิตเภท"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "4 วิธี ดูแผู้ป่วยจิตเภท",
                                    "text": "4 วิธี ดูแผู้ป่วยจิตเภท"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "การช่วยเหลือเบื้องต้นผู้มีอาการ",
                                    "text": "การช่วยเหลือเบื้องต้นผู้มีอาการโรคจิต"
                                }
                            },

                        ]
                    }
                }
            )
            line_bot_api.reply_message(self.replytoken, flex_message)
        if self.text == '7 สัญญาณเตือน ผู้ป่วยจิตเวชยาเสพติดก่อความรุนแรง':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630599635/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/7_%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%93%E0%B9%80%E0%B8%95%E0%B8%B7%E0%B8%AD%E0%B8%99_%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%9B%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%A7%E0%B8%8A%E0%B8%A2%E0%B8%B2%E0%B9%80%E0%B8%AA%E0%B8%9E%E0%B8%95%E0%B8%B4%E0%B8%94%E0%B8%81%E0%B9%88%E0%B8%AD%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B8%E0%B8%99%E0%B9%81%E0%B8%A3%E0%B8%87_mods4d.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630599635/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/7_%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%93%E0%B9%80%E0%B8%95%E0%B8%B7%E0%B8%AD%E0%B8%99_%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%9B%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%A7%E0%B8%8A%E0%B8%A2%E0%B8%B2%E0%B9%80%E0%B8%AA%E0%B8%9E%E0%B8%95%E0%B8%B4%E0%B8%94%E0%B8%81%E0%B9%88%E0%B8%AD%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B8%E0%B8%99%E0%B9%81%E0%B8%A3%E0%B8%87_mods4d.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == 'โรคจิตเภท':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630599780/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%A0%E0%B8%97_scfjkt.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630599780/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%A0%E0%B8%97_scfjkt.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == '4 วิธี ดูแผู้ป่วยจิตเภท':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630600017/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/4_%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5_%E0%B8%94%E0%B8%B9%E0%B9%81%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%9B%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%A0%E0%B8%97_cs9n8e.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630600017/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/4_%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5_%E0%B8%94%E0%B8%B9%E0%B9%81%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%9B%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%80%E0%B8%A0%E0%B8%97_cs9n8e.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == 'การช่วยเหลือเบื้องต้นผู้มีอาการโรคจิต':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630600259/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%8A%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B9%80%E0%B8%AB%E0%B8%A5%E0%B8%B7%E0%B8%AD%E0%B9%80%E0%B8%9A%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%95%E0%B9%89%E0%B8%99%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%A1%E0%B8%B5%E0%B8%AD%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%88%E0%B8%B4%E0%B8%95_eb3jug.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630600259/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%8A%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B9%80%E0%B8%AB%E0%B8%A5%E0%B8%B7%E0%B8%AD%E0%B9%80%E0%B8%9A%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%95%E0%B9%89%E0%B8%99%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%A1%E0%B8%B5%E0%B8%AD%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%88%E0%B8%B4%E0%B8%95_eb3jug.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == 'การดูแลผู้ป่วยซึมเศร้า':
            flex_message = FlexSendMessage(
                alt_text='hello',
                contents={
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "คุณเป็นโรคซึมเศร้าหรือไม่",
                                    "text": "คุณเป็นโรคซึมเศร้าหรือไม่"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "จะทำอย่างไรเมื่อเป็นโรคซึมเศร้า",
                                    "text": "จะทำอย่างไรเมื่อเป็นโรคซึมเศร้า"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "คนใกล้ชิด-สามารถช่วยได้",
                                    "text": "โรคซึมเศร้า-เพื่อน-ครอบครัว-คนใกล้ชิด-สามารถช่วยได้"
                                }
                            },
                        ]
                    }
                }
            )
            line_bot_api.reply_message(self.replytoken, flex_message)
        if self.text == 'คุณเป็นโรคซึมเศร้าหรือไม่':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630600858/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%8B%E0%B8%B6%E0%B8%A1%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%AB%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%84%E0%B8%A1%E0%B9%88_mb3ao6.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630600858/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%8B%E0%B8%B6%E0%B8%A1%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%AB%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%84%E0%B8%A1%E0%B9%88_mb3ao6.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == 'จะทำอย่างไรเมื่อเป็นโรคซึมเศร้า':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630601080/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%88%E0%B8%B0%E0%B8%97%E0%B8%B3%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B9%84%E0%B8%A3%E0%B9%80%E0%B8%A1%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%8B%E0%B8%B6%E0%B8%A1%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2_m4ji2v.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630601080/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%88%E0%B8%B0%E0%B8%97%E0%B8%B3%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B9%84%E0%B8%A3%E0%B9%80%E0%B8%A1%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%8B%E0%B8%B6%E0%B8%A1%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2_m4ji2v.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == 'โรคซึมเศร้า-เพื่อน-ครอบครัว-คนใกล้ชิด-สามารถช่วยได้':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630601466/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%84%E0%B8%99%E0%B9%83%E0%B8%81%E0%B8%A5%E0%B9%89%E0%B8%8A%E0%B8%B4%E0%B8%94-%E0%B8%AA%E0%B8%B2%E0%B8%A1%E0%B8%B2%E0%B8%A3%E0%B8%96%E0%B8%8A%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B9%84%E0%B8%94%E0%B9%89_z9rxhw.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630601466/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%84%E0%B8%99%E0%B9%83%E0%B8%81%E0%B8%A5%E0%B9%89%E0%B8%8A%E0%B8%B4%E0%B8%94-%E0%B8%AA%E0%B8%B2%E0%B8%A1%E0%B8%B2%E0%B8%A3%E0%B8%96%E0%B8%8A%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B9%84%E0%B8%94%E0%B9%89_z9rxhw.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == 'การจัดการความเครียด':
            flex_message = FlexSendMessage(
                alt_text='hello',
                contents={
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "การจัดการความเครียด",
                                    "text": "วิธีการจัดการความเครียด"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "3 ขั้นตอนฝึกสมาธิ คลายเครียด",
                                    "text": "3 ขั้นตอนฝึกสมาธิ คลายเครียด"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "7 วิธีฟื้นฟูใจตัวเอง",
                                    "text": "7 วิธีฟื้นฟูใจตัวเองจากการโดนนอกใจ"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "10 วิธีปฏิบัติเพื่อช่วยคลายเครียด",
                                    "text": "10 วิธีปฏิบัติเพื่อช่วยคลายเครียดในการทำงาน"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "ขั้นตอนการฝึกสติ",
                                    "text": "ขั้นตอนการฝึกสติ"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "การปฐมพยาบาลด้านสุขภาพจิต",
                                    "text": "การปฐมพยาบาลด้านสุขภาพจิต 1 รับ 4 ให้"
                                }
                            },
                        ]
                    }
                }
            )
            line_bot_api.reply_message(self.replytoken, flex_message)
        if self.text == 'วิธีการจัดการความเครียด':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630649395/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%94_ibtvvh.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630649395/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%94_ibtvvh.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == '3 ขั้นตอนฝึกสมาธิ คลายเครียด':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630649542/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/3_%E0%B8%82%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B8%9D%E0%B8%B6%E0%B8%81%E0%B8%AA%E0%B8%A1%E0%B8%B2%E0%B8%98%E0%B8%B4_%E0%B8%84%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%94_bizc7z.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630649542/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/3_%E0%B8%82%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B8%9D%E0%B8%B6%E0%B8%81%E0%B8%AA%E0%B8%A1%E0%B8%B2%E0%B8%98%E0%B8%B4_%E0%B8%84%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%94_bizc7z.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == '7 วิธีฟื้นฟูใจตัวเองจากการโดนนอกใจ':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630649769/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/7_%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%9F%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%9F%E0%B8%B9%E0%B9%83%E0%B8%88%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B9%80%E0%B8%AD%E0%B8%87%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%94%E0%B8%99%E0%B8%99%E0%B8%AD%E0%B8%81%E0%B9%83%E0%B8%88_nxtbxn.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630649769/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/7_%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%9F%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%9F%E0%B8%B9%E0%B9%83%E0%B8%88%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B9%80%E0%B8%AD%E0%B8%87%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%94%E0%B8%99%E0%B8%99%E0%B8%AD%E0%B8%81%E0%B9%83%E0%B8%88_nxtbxn.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == '10 วิธีปฏิบัติเพื่อช่วยคลายเครียดในการทำงาน':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630650044/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/10_%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%8A%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B8%84%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%B3%E0%B8%87%E0%B8%B2%E0%B8%99_q7ntyg.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630650044/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/10_%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%8A%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B8%84%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%B3%E0%B8%87%E0%B8%B2%E0%B8%99_q7ntyg.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == 'ขั้นตอนการฝึกสติ':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630650353/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%82%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9D%E0%B8%B6%E0%B8%81%E0%B8%AA%E0%B8%95%E0%B8%B4_lgzpcu.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630650353/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%82%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9D%E0%B8%B6%E0%B8%81%E0%B8%AA%E0%B8%95%E0%B8%B4_lgzpcu.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == 'การปฐมพยาบาลด้านสุขภาพจิต 1 รับ 4 ให้':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630650487/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%90%E0%B8%A1%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%A5%E0%B8%94%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%AA%E0%B8%B8%E0%B8%82%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%88%E0%B8%B4%E0%B8%95_1_%E0%B8%A3%E0%B8%B1%E0%B8%9A_4_%E0%B9%83%E0%B8%AB%E0%B9%89_ufves5.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630650487/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%90%E0%B8%A1%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%A5%E0%B8%94%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%AA%E0%B8%B8%E0%B8%82%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%88%E0%B8%B4%E0%B8%95_1_%E0%B8%A3%E0%B8%B1%E0%B8%9A_4_%E0%B9%83%E0%B8%AB%E0%B9%89_ufves5.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == 'การเฝ้าระวังความเสี่ยงฆ่าตัวตาย':
            flex_message = FlexSendMessage(
                alt_text='hello',
                contents={
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "5 สัญญาณเตือนเสี่ยงฆ่าตัวตาย",
                                    "text": "5 สัญญาณเตือนเสี่ยงฆ่าตัวตาย"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "รังแกกัน ไม่ใช่เรื่องล้อเล่น",
                                    "text": "กลั่นแกล้ง/รังแกกัน ไม่ใช่เรื่องล้อเล่น"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "10 สัญญานเตือนเสี่ยงฆ่าตัวตาย",
                                    "text": "10 สัญญานเตือนเสี่ยงฆ่าตัวตาย"
                                }
                            },
                            {
                                "type": "button",
                                "style": "secondary",
                                "action": {
                                    "type": "message",
                                    "label": "5อย่า3ควรเมื่อเห็นคนทำร้ายตัวเอง",
                                    "text": "5อย่า3ควรเมื่อเห็นคนทำร้ายตัวเอง"
                                }
                            },

                        ]
                    }
                }
            )
            line_bot_api.reply_message(self.replytoken, flex_message)
        if self.text == '5 สัญญาณเตือนเสี่ยงฆ่าตัวตาย':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630650948/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/5_%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%93%E0%B9%80%E0%B8%95%E0%B8%B7%E0%B8%AD%E0%B8%99%E0%B9%80%E0%B8%AA%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%87%E0%B8%86%E0%B9%88%E0%B8%B2%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B8%95%E0%B8%B2%E0%B8%A2_frxlwu.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630650948/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/5_%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%93%E0%B9%80%E0%B8%95%E0%B8%B7%E0%B8%AD%E0%B8%99%E0%B9%80%E0%B8%AA%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%87%E0%B8%86%E0%B9%88%E0%B8%B2%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B8%95%E0%B8%B2%E0%B8%A2_frxlwu.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == 'กลั่นแกล้ง/รังแกกัน ไม่ใช่เรื่องล้อเล่น':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630651100/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%81%E0%B8%A5%E0%B8%B1%E0%B9%88%E0%B8%99%E0%B9%81%E0%B8%81%E0%B8%A5%E0%B9%89%E0%B8%87_%E0%B8%A3%E0%B8%B1%E0%B8%87%E0%B9%81%E0%B8%81%E0%B8%81%E0%B8%B1%E0%B8%99_%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B9%83%E0%B8%8A%E0%B9%88%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B9%80%E0%B8%A5%E0%B9%88%E0%B8%99_w8solb.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630651100/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/%E0%B8%81%E0%B8%A5%E0%B8%B1%E0%B9%88%E0%B8%99%E0%B9%81%E0%B8%81%E0%B8%A5%E0%B9%89%E0%B8%87_%E0%B8%A3%E0%B8%B1%E0%B8%87%E0%B9%81%E0%B8%81%E0%B8%81%E0%B8%B1%E0%B8%99_%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B9%83%E0%B8%8A%E0%B9%88%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B9%80%E0%B8%A5%E0%B9%88%E0%B8%99_w8solb.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == '10 สัญญานเตือนเสี่ยงฆ่าตัวตาย':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630651338/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/10_%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%99%E0%B9%80%E0%B8%95%E0%B8%B7%E0%B8%AD%E0%B8%99%E0%B9%80%E0%B8%AA%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%87%E0%B8%86%E0%B9%88%E0%B8%B2%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B8%95%E0%B8%B2%E0%B8%A2_jzgowh.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630651338/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/10_%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%99%E0%B9%80%E0%B8%95%E0%B8%B7%E0%B8%AD%E0%B8%99%E0%B9%80%E0%B8%AA%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%87%E0%B8%86%E0%B9%88%E0%B8%B2%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B8%95%E0%B8%B2%E0%B8%A2_jzgowh.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
        if self.text == '5อย่า3ควรเมื่อเห็นคนทำร้ายตัวเอง':
            image_message = ImageSendMessage(
                original_content_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630652467/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/5%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B23%E0%B8%84%E0%B8%A7%E0%B8%A3%E0%B9%80%E0%B8%A1%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B9%80%E0%B8%AB%E0%B9%87%E0%B8%99%E0%B8%84%E0%B8%99%E0%B8%97%E0%B8%B3%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%A2%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B9%80%E0%B8%AD%E0%B8%87_wzoxxv.jpg',
                preview_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630652467/%E0%B9%80%E0%B8%81%E0%B8%A3%E0%B9%87%E0%B8%94%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89/5%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B23%E0%B8%84%E0%B8%A7%E0%B8%A3%E0%B9%80%E0%B8%A1%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B9%80%E0%B8%AB%E0%B9%87%E0%B8%99%E0%B8%84%E0%B8%99%E0%B8%97%E0%B8%B3%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%A2%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B9%80%E0%B8%AD%E0%B8%87_wzoxxv.jpg'
            )
            line_bot_api.reply_message(self.replytoken, image_message)
    def assessmentform(self):
        if self.text == 'แบบประเมิน':
            buttons_template_message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630676561/%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%A1%E0%B8%B4%E0%B8%99/%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%A1%E0%B8%B4%E0%B8%99_onya9z.png',
                    title='โรงพยาบาลจิตเวชขอนแก่นราชนครินทร์',
                    text='แบบประเมิน',
                    actions=[
                        URIAction(
                            label='แบบประเมินความเครียด',
                            uri='https://liff.line.me/1654982439-PGQy8pvw/st5'
                        ),
                        URIAction(
                            label='แบบประเมินการฆ่าตัวตาย',
                            uri='https://liff.line.me/1654982439-PGQy8pvw/q8'
                        ),
                        URIAction(
                            label='แบบประเมินโรคซึมเศร้า',
                            uri='https://liff.line.me/1654982439-PGQy8pvw/q9'
                        ),

                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, buttons_template_message)
    def assessmentformanswer(self):
        return self.replytoken
    def public_relations(self):
        if self.text == 'ติดต่อ ประชาสัมพันธ์':
            buttons_template_message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://res.cloudinary.com/dzldekasa/image/upload/v1630598588/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B9%82%E0%B8%A3%E0%B8%87%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%A5/OIyZlD_pex9uf.jpg',
                    title='โรงพยาบาลจิตเวชขอนแก่นราชนครินทร์',
                    text='169 ถนน ชาตะผดุง ตำบลในเมือง อำเภอเมืองขอนแก่น ขอนแก่น 40000',
                    actions=[
                        MessageAction(
                            label='เบอร์โทรติดต่อ - Email',
                            text='เบอร์โทรติดต่อ email'
                        ),
                        URIAction(
                            label='เว็บไซต์',
                            uri='http://www.jvkk.go.th:8080/web_jvkk_th/'
                        ),
                        MessageAction(
                            label='location',
                            text='location'
                        ),
                        URIAction(
                            label='KhuiKun : คุยกัน',
                            uri='https://line.me/R/ti/p/%40KhuiKun'
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(self.replytoken, buttons_template_message)
        if self.text == 'เบอร์โทรติดต่อ email':
            text_message = TextSendMessage(text='สายด่วนสุขภาพจิต : 1323\nรพ.จิตเวชขอนแก่นราชนครินทร์ : 043209999 \nEmail : careyou.jvkk@gmail.com ')
            line_bot_api.reply_message(self.replytoken, text_message)
        if self.text == 'location':
            location_message = LocationSendMessage(
                title='โรงพยาบาลจิตเวชขอนแก่นราชนครินทร์',
                address='169 ถนน ชาตะผดุง ตำบลในเมือง อำเภอเมืองขอนแก่น ขอนแก่น 40000',
                latitude=16.4257186,
                longitude=102.8489639
            )
            line_bot_api.reply_message(self.replytoken, location_message)
        if self.text == 'Email':
            text_message = TextSendMessage(text='Email : careyou.jvkk@gmail.com')
            line_bot_api.reply_message(self.replytoken, text_message)
        if self.text == 'เบอร์โทรติดต่อ':
            text_message = TextSendMessage(text='สายด่วนสุขภาพจิต : 1323\nรพ.จิตเวชขอนแก่นราชนครินทร์ : 043209999')
            line_bot_api.reply_message(self.replytoken, text_message)
    def fallback(self):
        text_message = TextSendMessage(text='ลองถามใหม่อีกครั้ง หรือเลือกเมนูข้างล่าง นะคะ',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="สอบถาม", text="สอบถามปัญหา")),
                                   QuickReplyButton(action=MessageAction(label="เตือนความจำ", text="เตือนความจำ")),
                                   QuickReplyButton(action=MessageAction(label="รู้เรื่องยา", text="รู้เรื่องยา")),
                                   QuickReplyButton(action=MessageAction(label="เกร็ดความรู้", text="เกร็ดความรู้")),
                                   QuickReplyButton(action=MessageAction(label="แบบประเมิน", text="แบบประเมิน")),
                                   QuickReplyButton(action=MessageAction(label="ติดต่อเรา", text="ติดต่อ ประชาสัมพันธ์")),
                               ]))
        line_bot_api.reply_message(self.replytoken, text_message)
    def __str__(self):
        return 'ok'


def intent_value(replytoken, intent, text, userid, body):
    que = Question(replytoken, intent, text, userid, body)
    if intent == 'Question':
        que.question()
    if intent == 'Question - fallback':
        que.questionfallback()
    if intent == 'Menu' or 'Menu - yes':
        que.menu()
    if intent == 'Reminder':
        que.reminder()
    if intent == 'AssessmentForm':
        que.assessmentform()
    if intent == 'AssessmentFormAnswer':
        que.assessmentformanswer()
    if intent == 'Knowledge':
        que.knowledge()
    if intent == 'Public relations':
        que.public_relations()
    if intent == 'Drug':
        que.drug()
    if intent == 'Default Fallback Intent':
        que.fallback()
    else:
        que.reply()
