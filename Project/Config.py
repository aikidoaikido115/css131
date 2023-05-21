import os
from dotenv import load_dotenv

load_dotenv()
Channel_secret = os.getenv('ENV_Channel_secret')
Channel_access_token = os.getenv('ENV_Channel_access_token')
basic_id = os.getenv('ENV_basic_id')


# data = [('name1', 'link1', 'image1'),('name2', 'link2', 'image2'),('name3', 'link3', 'image3'),......,('name n', 'link n', 'image n')] 


def Flex_New(data):
  url = [i[1] for i in data]
  clean_url = ['https://'+i[2:] for i in url]
  # print(clean_url)
  return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": data[0][2],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#FFFECAFF",
        "borderColor": "#FFFECAFF",
        "contents": [
          {
            "type": "text",
            "text": data[0][0],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#FFFECAFF",
        "borderColor": "#FFFECAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "ดูเรื่องนี้คลิก",
              "uri": clean_url[0]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": data[1][2],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#FFFECAFF",
        "borderColor": "#FFFECAFF",
        "contents": [
          {
            "type": "text",
            "text": data[1][0],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#FFFECAFF",
        "borderColor": "#FFFECAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "ดูเรื่องนี้คลิก",
              "uri": clean_url[1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": data[2][2],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#FFFECAFF",
        "borderColor": "#FFFECAFF",
        "contents": [
          {
            "type": "text",
            "text": data[2][0],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#FFFECAFF",
        "borderColor": "#FFFECAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "ดูเรื่องนี้คลิก",
              "uri": clean_url[2]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": data[3][2],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#FFFECAFF",
        "borderColor": "#FFFECAFF",
        "contents": [
          {
            "type": "text",
            "text": data[3][0],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#FFFECAFF",
        "borderColor": "#FFFECAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "ดูเรื่องนี้คลิก",
              "uri": clean_url[3]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": data[4][2],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#FFFECAFF",
        "borderColor": "#FFFECAFF",
        "contents": [
          {
            "type": "text",
            "text": data[4][0],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#FFFECAFF",
        "borderColor": "#FFFECAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "ดูเรื่องนี้คลิก",
              "uri": clean_url[4]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "See more",
              "uri": "https://www.bilibili.tv/th/category?season_type=1,4&order=2&area_id=2&style_id=-1"
            },
            "flex": 1,
            "gravity": "center"
          }
        ]
      },
      "styles": {
        "body": {
          "backgroundColor": "#FFFECAFF",
          "separatorColor": "#FFFECAFF"
        }
      }
    }
  ]
}


def Flex_Genre():
  return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "text",
            "text": "Action",
            "weight": "bold",
            "size": "xxl",
            "color": "#000000FF",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ค้นหาแนวนี้คลิก",
              "text": "Action"
            },
            "color": "#000000FF",
            "style": "primary"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "text",
            "text": "Sci-fi",
            "weight": "bold",
            "size": "xxl",
            "color": "#000000FF",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ค้นหาแนวนี้คลิก",
              "text": "Sci-fi"
            },
            "color": "#000000FF",
            "style": "primary"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "text",
            "text": "Comedy",
            "weight": "bold",
            "size": "xxl",
            "color": "#000000FF",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ค้นหาแนวนี้คลิก",
              "text": "Comedy"
            },
            "color": "#000000FF",
            "style": "primary"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "text",
            "text": "Yuri",
            "weight": "bold",
            "size": "xxl",
            "color": "#000000FF",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ค้นหาแนวนี้คลิก",
              "text": "Yuri"
            },
            "color": "#000000FF",
            "style": "primary"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "text",
            "text": "Music",
            "weight": "bold",
            "size": "xxl",
            "color": "#000000FF",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ค้นหาแนวนี้คลิก",
              "text": "Music"
            },
            "color": "#000000FF",
            "style": "primary"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "text",
            "text": "Drama",
            "weight": "bold",
            "size": "xxl",
            "color": "#000000FF",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ค้นหาแนวนี้คลิก",
              "text": "Drama"
            },
            "color": "#000000FF",
            "style": "primary"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "text",
            "text": "Harem",
            "weight": "bold",
            "size": "xxl",
            "color": "#000000FF",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ค้นหาแนวนี้คลิก",
              "text": "Harem"
            },
            "color": "#000000FF",
            "style": "primary"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "text",
            "text": "Romance",
            "weight": "bold",
            "size": "xxl",
            "color": "#000000FF",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ค้นหาแนวนี้คลิก",
              "text": "Romance"
            },
            "color": "#000000FF",
            "style": "primary"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "text",
            "text": "Fantasy",
            "weight": "bold",
            "size": "xxl",
            "color": "#000000FF",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ค้นหาแนวนี้คลิก",
              "text": "Fantasy"
            },
            "color": "#000000FF",
            "style": "primary"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "backgroundColor": "#D0FAEAFF",
        "borderColor": "#D0FAEAFF",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "See more",
              "uri": "https://www.bilibili.tv/th/category?season_type=1,4&order=0"
            },
            "flex": 1,
            "gravity": "center"
          }
        ]
      }
    }
  ]
}

if __name__ == '__main__':
  print("Misha Necron debuggggggggg")