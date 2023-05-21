

from flask import Flask, request, abort
# import requests
# import json
from Project.Config import *
from Add_ons.add_ons import *


app = Flask(__name__)


@app.route('/webhook', methods = ['POST', 'GET'])
def webhook():
    if request.method == 'POST':

        payload = request.json
        print(payload)

        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)

        message = payload['events'][0]['message']['text']


        if "อนิเมะใหม่" in message :
            data = BiliBili()
            ReplyFlexAnimeName(Reply_token, data, Channel_access_token)

        elif "tag" in message :
            data = 'fool'
            ReplyFlexGenre(Reply_token, data, Channel_access_token)

        category = {
            "Action": {"url": "https://www.bilibili.tv/th/category?season_type=1,4&style_id=11001&order=0&area_id=2"},
            "Sci-fi": {"url": "https://www.bilibili.tv/th/category?season_type=1,4&style_id=71&order=0&area_id=2"},
            "Comedy": {"url": "https://www.bilibili.tv/th/category?season_type=1,4&style_id=11003&order=0&area_id=2"},
            "Yuri": {"url": "https://www.bilibili.tv/th/category?season_type=1,4&style_id=10002&order=0&area_id=2"},
            "Music": {"url": "https://www.bilibili.tv/th/category?season_type=1,4&style_id=72&order=0&area_id=2"},
            "Drama": {"url": "https://www.bilibili.tv/th/category?season_type=1,4&style_id=11004&order=0&area_id=2"},
            "Harem": {"url": "https://www.bilibili.tv/th/category?season_type=1,4&style_id=5&order=0&area_id=2"},
            "Romance": {"url": "https://www.bilibili.tv/th/category?season_type=1,4&style_id=11007&order=0&area_id=2"},
            "Fantasy": {"url": "https://www.bilibili.tv/th/category?season_type=1,4&style_id=57&order=0&area_id=2"}
            }
        
        if message in category:
            data = BiliBili(url=category[message]["url"])
            ReplyFlexAnimeName(Reply_token, data, Channel_access_token)


        return request.json, 200

    elif request.method == 'GET':
        return 'this is method GET!!!', 200
    
    else:
        abort(400)

@app.route('/')
def hello():
    return 'Misha Necron', 200


#test
# def ReplyMessage(Reply_token, TextMessage, Line_Access_Token):
#     LINE_API = 'https://api.line.me/v2/bot/message/reply'

#     Authorization = 'Bearer {}'.format(Line_Access_Token) ##ที่ยาวๆ
#     print(Authorization)
#     headers = {
#         'Content-Type': 'application/json; charset=UTF-8',
#         'Authorization':Authorization
#     }

#     data = {
#         "replyToken":Reply_token,
#         "messages":[{
#             "type":"text",
#             "text":TextMessage
#         }]
#     }

#     data = json.dumps(data) ## dump dict >> Json Object
#     r = requests.post(LINE_API, headers=headers, data=data) 
#     return 200