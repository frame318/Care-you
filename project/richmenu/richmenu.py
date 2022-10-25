from linebot import *
from linebot.exceptions import *
from linebot.models import *
from linebot.models.actions import *
from linebot.models.rich_menu import *

line_bot_api = LineBotApi('Hk+4eFuOHBD7EN38YB5FvmlpGvgL7SAa2QWV50gvuUZ4JOeiUqfKMweft3wF1Sv6ilyqmPM+JqsHFWlBVkI9uUItXjxtwc5e1K0hhyp3mqgOwXHJ4ecLGigMwoHuME8HLOr0LNWHx9FhnRhiGubIxAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('238aa62de84ad9065acba684eb1df163')


# rich_menu_to_create = RichMenu(
#     size=RichMenuSize(width=2500, height=843),
#     selected=True,
#     name="richmenu",
#     chat_bar_text="สอบถามปัญหา",
#     areas=[RichMenuArea(
#         bounds=RichMenuBounds(x=1614, y=504, width=886, height=339),
#         action=MessageAction(label="message", text="เมนูหลัก"))]
# )
# rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
# print(rich_menu_id)
#
# with open('richmenu.jpg', 'rb') as f:
#     line_bot_api.set_rich_menu_image(rich_menu_id, 'image/jpeg', f)

# line_bot_api.delete_rich_menu(rich_menu_id)
# richmenu-72a16f5b0c0fcfd3fa814be8edc1b616
# richmenu-d115e26182c89b25468c6882416fd139


# rich_menu_to_create = RichMenu(
#     size=RichMenuSize(width=2500, height=1686),
#     selected=True,
#     name="richmenu",
#     chat_bar_text="กดเพื่อดูเมนู",
#     areas=[
#     RichMenuArea(
#         bounds=RichMenuBounds(x=0, y=4, width=822, height=839),
#         action=MessageAction(label="message", text="สอบถามปัญหา")),
#     RichMenuArea(
#         bounds=RichMenuBounds(x=839, y=13, width=814, height=826),
#         action=MessageAction(label="message", text="เตือนความจำ")),
#     RichMenuArea(
#         bounds=RichMenuBounds(x=1674, y=13, width=826, height=822),
#         action=MessageAction(label="message", text="รู้เรื่องยา")),
#     RichMenuArea(
#         bounds=RichMenuBounds(x=0, y=860, width=822, height=826),
#         action=MessageAction(label="message", text="เกร็ดความรู้")),
#     RichMenuArea(
#         bounds=RichMenuBounds(x=847, y=852, width=806, height=834),
#         action=MessageAction(label="message", text="แบบประเมิน")),
#     RichMenuArea(
#         bounds=RichMenuBounds(x=1682, y=847, width=818, height=839),
#         action=MessageAction(label="message", text="ติดต่อ ประชาสัมพันธ์")),
#         ]
# )
# rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
# print(rich_menu_id)
#
# with open('richmenu_main.jpg', 'rb') as f:
#     line_bot_api.set_rich_menu_image(rich_menu_id, 'image/jpeg', f)

# richmenu-4a56674b3aaf2ecd6a608e90cc66c61a
