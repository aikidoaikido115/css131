


import requests
from bs4 import BeautifulSoup
import json
from Project.Config import *



def ReplyFlexAnimeName(Reply_token, data, Line_Access_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Access_Token) ##ที่ยาวๆ
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"flex",
            "altText":"~~SUGGESTION~~",
            "contents": Flex_New(data)
        }]}
        
    print(data)

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200


def ReplyFlexGenre(Reply_token, data, Line_Access_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Access_Token) ##ที่ยาวๆ
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"flex",
            "altText":"~~GENRE~~",
            "contents": Flex_Genre()
        }]}
        
    print(data)

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200

def Broadcast(data, Line_Access_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/broadcast'
    broadcast_content = BiliBili()

    Authorization = 'Bearer {}'.format(Line_Access_Token) ##ที่ยาวๆ
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
        
    }

    data = {
        "messages":[{
            "type":"flex",
            "altText":"~~SUGGESTION~~",
            "contents": Flex_New(broadcast_content)
        }]}
        
    print(data)

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200




def BiliBili(url='https://www.bilibili.tv/th/category?season_type=1,4&order=2&area_id=2&style_id=-1'):
    r = requests.get(url)
    soup =  BeautifulSoup(r.text, 'html.parser')
    find_name_or_url = soup.find_all('a',{'class':'bstar-video-card__title-text'})
    find_image_url = soup.find_all('img',{'class':'bstar-image__img'})
    
    name_list = []
    url_list = []
    image_url_list = []


    # for i in find_name_or_url:
    #     name = i.text.encode('ISO-8859-1').decode('utf-8')
    #     URL = i['href']
    #     name_list.append(name)
    #     url_list.append(URL)

    # for i in find_image_url:
    #     image_src = i['src']
    #     image_url_list.append(image_src)


    for i, j in zip(find_name_or_url, find_image_url):
        name = i.text.encode('ISO-8859-1').decode('utf-8')
        URL = i['href']
        image_src = j['src']

        name_list.append(name)
        url_list.append(URL)
        image_url_list.append(image_src)

    # print(find_image_url[0]['src'])

    

    return list(zip(name_list, url_list, image_url_list))

#debug
if __name__ == '__main__':
    print(BiliBili())
    