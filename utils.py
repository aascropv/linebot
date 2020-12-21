import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    # line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    if (text == "Trigger state1"):
        # message = TextSendMessage(text = 'Hello world')
        message2 = TextSendMessage(text = 'https://www.learncodewithmike.com/2020/07/python-web-scraping-line-bot.html')
        print("test state1")
        # line_bot_api.reply_message(reply_token, message)
        line_bot_api.reply_message(reply_token, message2)
    # elif (text == "Trigger state2"):
        # message = ImageSendMessage(
        #     original_content_url = '',
        #     preview_image_url = ''
        # )
        # line_bot_api.reply_message(reply_token, message)
    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
