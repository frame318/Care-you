from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import requests

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import *
from linebot.models import *

from .question import *

import base64
import hashlib
import hmac

line_bot_api = LineBotApi('Hk+4eFuOHBD7EN38YB5FvmlpGvgL7SAa2QWV50gvuUZ4JOeiUqfKMweft3wF1Sv6ilyqmPM+JqsHFWlBVkI9uUItXjxtwc5e1K0hhyp3mqgOwXHJ4ecLGigMwoHuME8HLOr0LNWHx9FhnRhiGubIxAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('238aa62de84ad9065acba684eb1df163')
channel_secret = '238aa62de84ad9065acba684eb1df163'
# Create your views here.

# LINE
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        if 'X-Line-Signature' in request.headers:

            body = request.body.decode('utf-8')
            hash = hmac.new(channel_secret.encode('utf-8'),body.encode('utf-8'), hashlib.sha256).digest()
            signature_check = base64.b64encode(hash).decode()

            signature = request.headers['X-Line-Signature']

            if signature == signature_check:
                print('>> X-Line-Signature Success! (LINE) <<')
                body=json.loads(request.body)
                # print(body)
                if body['events'][0]['type'] == 'follow':
                    print('follow')
                    userid = body['destination']
                    return HttpResponse('200')
                if body['events'][0]['type'] == 'unfollow':
                    print('unfollow')
                    return HttpResponse('200')
                else:
                    userid = body['events'][0]['source']['userId']
                    replytoken = body['events'][0]['replyToken']
                    type_text = body['events'][0]['message']['type']
                    if type_text == 'sticker':
                        # keywords = body['events'][0]['message']['keywords'] # ประเภท sticker
                        body['events'][0]['message']['type'] = 'text'
                        body['events'][0]['message']['text'] = 'sticker'
                        url = 'https://dialogflow.cloud.google.com/v1/integrations/line/webhook/77f60b10-de96-4c59-808d-d6c5d37e5127'
                        x = requests.post(url, json=body)
                    else:
                        url = 'https://dialogflow.cloud.google.com/v1/integrations/line/webhook/77f60b10-de96-4c59-808d-d6c5d37e5127'
                        x = requests.post(url, json=body)

                    return HttpResponse('200')
            else:
                return HttpResponse('X-Line-Signature Error')
        else:
            return HttpResponse('Not X-Line-Signature')
    else:
        return HttpResponse('404')

# Dialogflow
@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        if 'X-Line-Signature' in request.headers:
            signature = request.headers['X-Line-Signature']
            if signature == channel_secret:
                print('>> X-Line-Signature Success! (Dialogflow) <<')
                body=json.loads(request.body)
                # print(body)
                intent = body['queryResult']['intent']['displayName']
                text = body['originalDetectIntentRequest']['payload']['data']['message']['text']
                userid = body['originalDetectIntentRequest']['payload']['data']['source']['userId']
                replytoken = body['originalDetectIntentRequest']['payload']['data']['replyToken']

                intent_value(replytoken, intent, text, userid, body)

                return HttpResponse('200')
            else:
                return HttpResponse('X-Line-Signature Error')
        else:
            return HttpResponse('Not X-Line-Signature')
    else:
        return HttpResponse('404')
