import os

from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, PostbackTemplateAction, MessageTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ButtonsTemplate

load_dotenv()

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"

def send_image_url(reply_token, img_url1):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url=img_url1,
        preview_image_url=img_url1
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"

def send_template_message_hololive(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/KsnMcp4/talent2.jpg',
                    title='hololive talent',
                    text='hololive 0期生(藝人)介紹',
                    actions=[
                        MessageTemplateAction(
                            label='零期生介紹',
                            text='HololiveTalent'
                        ),
                        URITemplateAction(
                            label='零期生圖片',
                            uri='https://i.ibb.co/yqfQ28X/talent.jpg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/mcYhC3t/1st-generation.jpg',
                    title='hololive 1st generation',
                    text='hololive 1期生介紹',
                    actions=[
                        MessageTemplateAction(
                            label='一期生介紹',
                            text='Hololive1st'
                        ),
                        URITemplateAction(
                            label='一期生圖片',
                            uri='https://i.ibb.co/wdCnM9M/1st-generation2.jpg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/GT5FYGP/2nd-generation.jpg',
                    title='hololive 2nd generation',
                    text='hololive 2期生介紹',
                    actions=[
                        MessageTemplateAction(
                            label='二期生介紹',
                            text='Hololive2nd'
                        ),
                        URITemplateAction(
                            label='二期生圖片',
                            uri='https://i.ibb.co/PQZvfWW/2nd-generation2.jpg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/Tq6XM3D/gamers.png',
                    title='hololive gamers',
                    text='hololive gamers介紹',
                    actions=[
                        MessageTemplateAction(
                            label='Gamers介紹',
                            text='HololiveGamers'
                        ),
                        URITemplateAction(
                            label='Gamers圖片',
                            uri='https://i.ibb.co/n3x7Cgy/gamers1.jpg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/KNxJKQt/3rd-generation2.jpg',
                    title='hololive 3rd generation',
                    text='hololive 3期生介紹',
                    actions=[
                        MessageTemplateAction(
                            label='三期生介紹',
                            text='Hololive3rd'
                        ),
                        URITemplateAction(
                            label='三期生圖片',
                            uri='https://i.ibb.co/8MGzVb1/3rd-generation3.jpg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/J2f2pXP/4th-generation.jpg',
                    title='hololive 4th generation',
                    text='hololive 4期生介紹',
                    actions=[
                        MessageTemplateAction(
                            label='四期生介紹',
                            text='Hololive4th'
                        ),
                        URITemplateAction(
                            label='四期生圖片',
                            uri='https://i.ibb.co/xSLZBWG/4th-generation2.jpg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/K6T45GX/5th-generation2.jpg',
                    title='hololive 5th generation',
                    text='hololive 5期生介紹',
                    actions=[
                        MessageTemplateAction(
                            label='五期生介紹',
                            text='Hololive5th'
                        ),
                        URITemplateAction(
                            label='五期生圖片',
                            uri='https://i.ibb.co/wsTT150/5th-generation.jpg'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return 'OK'

def send_carousel_template_holo_talent(reply_token):
    line_bot_api=LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/0rR1tgW/sora.jpg',
                    title='時乃空',
                    text='時乃空',
                    actions=[
                        MessageTemplateAction(
                            label='時乃空簡介',
                            text='時乃空簡介'
                        ),
                        URITemplateAction(
                            label='時乃空Youtube',
                            uri='https://www.youtube.com/channel/UCp6993wxpyDPHUpavwDFqgg'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/sP4t5pt/miko.jpg',
                    title='櫻巫女',
                    text='櫻巫女',
                    actions=[
                        MessageTemplateAction(
                            label='櫻巫女簡介',
                            text='櫻巫女簡介'
                        ),
                        URITemplateAction(
                            label='櫻巫女Youtube',
                            uri='https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/k1dKGsQ/suisei.jpg',
                    title='星街彗星',
                    text='星街彗星',
                    actions=[
                        MessageTemplateAction(
                            label='星街彗星簡介',
                            text='星街彗星簡介'
                        ),
                        URITemplateAction(
                            label='星街彗星Youtube',
                            uri='https://www.youtube.com/channel/UC5CwaMl1eIgY8h02uZw7u8A'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/GQTCj5j/roboco2.jpg',
                    title='蘿蔔子',
                    text='蘿蔔子',
                    actions=[
                        MessageTemplateAction(
                            label='蘿蔔子簡介',
                            text='蘿蔔子簡介'
                        ),
                        URITemplateAction(
                            label='蘿蔔子Youtube',
                            uri='https://www.youtube.com/channel/UCDqI2jOz0weumE8s7paEk6g'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return 'OK'

def send_carousel_template_holo1st(reply_token):
    line_bot_api=LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/zFhtKKN/fubuki.jpg',
                    title='白上吹雪',
                    text='白上吹雪',
                    actions=[
                        MessageTemplateAction(
                            label='白上吹雪簡介',
                            text='白上吹雪簡介'
                        ),
                        URITemplateAction(
                            label='白上吹雪Youtube',
                            uri='https://www.youtube.com/channel/UCdn5BQ06XqgXoAxIhbqw5Rg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/PNFvxwR/matsuri.jpg',
                    title='夏色祭',
                    text='夏色祭',
                    actions=[
                        MessageTemplateAction(
                            label='夏色祭簡介',
                            text='夏色祭簡介'
                        ),
                        URITemplateAction(
                            label='夏色祭Youtube',
                            uri='https://www.youtube.com/channel/UCQ0UDLQCjY0rmuxCDE38FGg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/6Nm7QHK/haato.jpg',
                    title='赤井心',
                    text='赤井心',
                    actions=[
                        MessageTemplateAction(
                            label='赤井心簡介',
                            text='赤井心簡介'
                        ),
                        URITemplateAction(
                            label='赤井心Youtube',
                            uri='https://www.youtube.com/channel/UC1CfXB_kRs3C-zaeTG3oGyg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/kSWy2Rj/mel2.jpg',
                    title='夜空梅露',
                    text='夜空梅露',
                    actions=[
                        MessageTemplateAction(
                            label='夜空梅露簡介',
                            text='夜空梅露簡介'
                        ),
                        URITemplateAction(
                            label='夜空梅露Youtube',
                            uri='https://www.youtube.com/channel/UCD8HOxPs4Xvsm8H0ZxXGiBw'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/X39JjGy/akirosenthal.jpg',
                    title='亞綺．羅森塔爾',
                    text='亞綺．羅森塔爾',
                    actions=[
                        MessageTemplateAction(
                            label='亞綺．羅森塔爾簡介',
                            text='亞綺．羅森塔爾簡介'
                        ),
                        URITemplateAction(
                            label='亞綺．羅森塔爾Youtube',
                            uri='https://www.youtube.com/channel/UCFTLzh12_nrtzqBPsTCqenA'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return 'OK'

def send_carousel_template_holo2nd(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/vJ6vxgz/ayame2.jpg',
                    title='百鬼綾目',
                    text='百鬼綾目',
                    actions=[
                        MessageTemplateAction(
                            label='百鬼綾目簡介',
                            text='百鬼綾目簡介'
                        ),
                        URITemplateAction(
                            label='百鬼綾目Youtube',
                            uri='https://www.youtube.com/channel/UC7fk0CB07ly8oSl0aqKkqFg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/9sNQ4pK/aqua.jpg',
                    title='湊阿庫婭',
                    text='湊阿庫婭',
                    actions=[
                        MessageTemplateAction(
                            label='湊阿庫婭簡介',
                            text='湊阿庫婭簡介'
                        ),
                        URITemplateAction(
                            label='湊阿庫婭Youtube',
                            uri='https://www.youtube.com/channel/UC1opHUrw8rvnsadT-iGp7Cg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/NnBfsnp/shion.jpg',
                    title='紫咲詩音',
                    text='紫咲詩音',
                    actions=[
                        MessageTemplateAction(
                            label='紫咲詩音簡介',
                            text='紫咲詩音簡介'
                        ),
                        URITemplateAction(
                            label='紫咲詩音Youtube',
                            uri='https://www.youtube.com/channel/UCXTpFs_3PqI41qX2d9tL2Rw'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/ng6LHQT/choco.jpg',
                    title='癒月巧可',
                    text='癒月巧可',
                    actions=[
                        MessageTemplateAction(
                            label='癒月巧可簡介',
                            text='癒月巧可簡介'
                        ),
                        URITemplateAction(
                            label='癒月巧可Youtube',
                            uri='https://www.youtube.com/channel/UC1suqwovbL1kzsoaZgFZLKg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/C0nY7G0/subaru.jpg',
                    title='大空昴',
                    text='大空昴',
                    actions=[
                        MessageTemplateAction(
                            label='大空昴簡介',
                            text='大空昴簡介'
                        ),
                        URITemplateAction(
                            label='大空昴Youtube',
                            uri='https://www.youtube.com/channel/UCvzGlP9oQwU--Y0r9id_jnA'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return 'OK'

def send_carousel_template_holo_gamers(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/zFhtKKN/fubuki.jpg',
                    title='白上吹雪',
                    text='白上吹雪',
                    actions=[
                        MessageTemplateAction(
                            label='白上吹雪簡介',
                            text='白上吹雪簡介'
                        ),
                        URITemplateAction(
                            label='白上吹雪Youtube',
                            uri='https://www.youtube.com/channel/UCdn5BQ06XqgXoAxIhbqw5Rg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/JrJJRMJ/okayu3.jpg',
                    title='貓又小粥',
                    text='貓又小粥',
                    actions=[
                        MessageTemplateAction(
                            label='貓又小粥簡介',
                            text='貓又小粥簡介'
                        ),
                        URITemplateAction(
                            label='貓又小粥Youtube',
                            uri='https://www.youtube.com/channel/UCvaTdHTWBGv3MKj3KVqJVCw'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/CVKmK0t/korone.jpg',
                    title='戌神沁音',
                    text='戌神沁音',
                    actions=[
                        MessageTemplateAction(
                            label='戌神沁音簡介',
                            text='戌神沁音簡介'
                        ),
                        URITemplateAction(
                            label='戌神沁音Youtube',
                            uri='https://www.youtube.com/channel/UChAnqc_AY5_I3Px5dig3X1Q'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/kXJP686/mio.jpg',
                    title='大神澪',
                    text='大神澪',
                    actions=[
                        MessageTemplateAction(
                            label='大神澪簡介',
                            text='大神澪簡介'
                        ),
                        URITemplateAction(
                            label='大神澪Youtube',
                            uri='https://www.youtube.com/channel/UCp-5t9SrOQwXMU7iIjQfARg'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return 'OK'

def send_carousel_template_holo3rd(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/GtPRPxj/pekora2-1.jpg',
                    title='兔田佩可拉',
                    text='兔田佩可拉',
                    actions=[
                        MessageTemplateAction(
                            label='兔田佩可拉簡介',
                            text='兔田佩可拉簡介'
                        ),
                        URITemplateAction(
                            label='兔田佩可拉Youtube',
                            uri='https://www.youtube.com/channel/UC1DCedRgGHBdm81E1llLhOQ'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/NFBzjm6/EYTTINx-Uw-AMi39z.jpg',
                    title='寶鐘瑪琳',
                    text='寶鐘瑪琳',
                    actions=[
                        MessageTemplateAction(
                            label='寶鐘瑪琳簡介',
                            text='寶鐘瑪琳簡介'
                        ),
                        URITemplateAction(
                            label='寶鐘瑪琳Youtube',
                            uri='https://www.youtube.com/channel/UCCzUftO8KOVkV4wQG1vkUvg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/XxMdMRx/rushia.jpg',
                    title='潤羽露西亞',
                    text='潤羽露西亞',
                    actions=[
                        MessageTemplateAction(
                            label='潤羽露西亞簡介',
                            text='潤羽露西亞簡介'
                        ),
                        URITemplateAction(
                            label='潤羽露西亞Youtube',
                            uri='https://www.youtube.com/channel/UCl_gCybOJRIgOXw6Qb4qJzQ'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/LCd2bj1/noel2.jpg',
                    title='白銀諾艾爾',
                    text='白銀諾艾爾',
                    actions=[
                        MessageTemplateAction(
                            label='白銀諾艾爾簡介',
                            text='白銀諾艾爾簡介'
                        ),
                        URITemplateAction(
                            label='白銀諾艾爾Youtube',
                            uri='https://www.youtube.com/channel/UCdyqAaZDKHXg4Ahi7VENThQ'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/r34sKdJ/flare2.jpg',
                    title='不知火芙蕾雅',
                    text='不知火芙蕾雅',
                    actions=[
                        MessageTemplateAction(
                            label='不知火芙蕾雅簡介',
                            text='不知火芙蕾雅簡介'
                        ),
                        URITemplateAction(
                            label='不知火芙蕾雅Youtube',
                            uri='https://www.youtube.com/channel/UCvInZx9h3jC2JzsIzoOebWg'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return 'OK'

def send_carousel_template_holo4th(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/mXSJfbV/watame.jpg',
                    title='角卷綿芽',
                    text='角卷綿芽',
                    actions=[
                        MessageTemplateAction(
                            label='角卷綿芽簡介',
                            text='角卷綿芽簡介'
                        ),
                        URITemplateAction(
                            label='角卷綿芽Youtube',
                            uri='https://www.youtube.com/channel/UCqm3BQLlJfvkTsX_hvm0UmA'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/tHqV5NP/coco2.jpg',
                    title='桐生可可',
                    text='桐生可可',
                    actions=[
                        MessageTemplateAction(
                            label='桐生可可簡介',
                            text='桐生可可簡介'
                        ),
                        URITemplateAction(
                            label='桐生可可Youtube',
                            uri='https://www.youtube.com/channel/UCS9uQI-jC3DE0L4IpXyvr6w'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/C88xx53/kanata2.jpg',
                    title='天音彼方',
                    text='天音彼方',
                    actions=[
                        MessageTemplateAction(
                            label='天音彼方簡介',
                            text='天音彼方簡介'
                        ),
                        URITemplateAction(
                            label='天音彼方Youtube',
                            uri='https://www.youtube.com/channel/UCZlDXzGoo7d44bwdNObFacg'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/55q0GH8/Towa.jpg',
                    title='常闇永遠',
                    text='常闇永遠',
                    actions=[
                        MessageTemplateAction(
                            label='常闇永遠簡介',
                            text='常闇永遠簡介'
                        ),
                        URITemplateAction(
                            label='常闇永遠Youtube',
                            uri='https://www.youtube.com/channel/UC1uv2Oq6kNxgATlCiez59hw'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/nrdn6Wb/luna.jpg',
                    title='姬森璐娜',
                    text='姬森璐娜',
                    actions=[
                        MessageTemplateAction(
                            label='姬森璐娜簡介',
                            text='姬森璐娜簡介'
                        ),
                        URITemplateAction(
                            label='姬森璐娜Youtube',
                            uri='https://www.youtube.com/channel/UCa9Y57gfeY0Zro_noHRVrnw'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return 'OK'

def send_carousel_template_holo5th(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/0Vh3B9n/lamy.jpg',
                    title='雪花菈米',
                    text='雪花菈米',
                    actions=[
                        MessageTemplateAction(
                            label='雪花菈米簡介',
                            text='雪花菈米簡介'
                        ),
                        URITemplateAction(
                            label='雪花菈米Youtube',
                            uri='https://www.youtube.com/channel/UCFKOVgVbGmX65RxO3EtH3iw'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/4p3Dgbm/botan.jpg',
                    title='獅白牡丹',
                    text='獅白牡丹',
                    actions=[
                        MessageTemplateAction(
                            label='獅白牡丹簡介',
                            text='獅白牡丹簡介'
                        ),
                        URITemplateAction(
                            label='獅白牡丹Youtube',
                            uri='https://www.youtube.com/channel/UCUKD-uaobj9jiqB-VXt71mA'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/r5tZZW7/nene.jpg',
                    title='桃鈴音音',
                    text='桃鈴音音',
                    actions=[
                        MessageTemplateAction(
                            label='桃鈴音音簡介',
                            text='桃鈴音音簡介'
                        ),
                        URITemplateAction(
                            label='桃鈴音音Youtube',
                            uri='https://www.youtube.com/channel/UCAWSyEs_Io8MtpY3m-zqILA'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/Ph9Bf4p/polka.jpg',
                    title='尾丸波爾卡',
                    text='尾丸波爾卡',
                    actions=[
                        MessageTemplateAction(
                            label='尾丸波爾卡簡介',
                            text='尾丸波爾卡簡介'
                        ),
                        URITemplateAction(
                            label='尾丸波爾卡Youtube',
                            uri='https://www.youtube.com/channel/UCK9V2B22uJYu3N7eR_BT9QA'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/5xNSBRc/aloe.png',
                    title='魔乃阿蘿耶(卒業)',
                    text='魔乃阿蘿耶(卒業)',
                    actions=[
                        MessageTemplateAction(
                            label='魔乃阿蘿耶(卒業)簡介',
                            text='魔乃阿蘿耶(卒業)簡介'
                        ),
                        URITemplateAction(
                            label='魔乃阿蘿耶(卒業)Youtube',
                            uri='https://www.youtube.com/channel/UCgZuwn-O7Szh9cAgHqJ6vjw/channels'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return 'OK'

def send_members_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    if text == '時乃空簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/zh-tw/%E6%97%B6%E4%B9%83%E7%A9%BA")
    elif text == '櫻巫女簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/zh-tw/%E6%A8%B1%E5%B7%AB%E5%A5%B3")
    elif text == '星街彗星簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/zh-tw/%E6%98%9F%E8%A1%97%E5%BD%97%E6%98%9F")
    elif text == '蘿蔔子簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E8%90%9D%E5%8D%9C%E5%AD%90")
    elif text == '白上吹雪簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E7%99%BD%E4%B8%8A%E5%90%B9%E9%9B%AA")
    elif text == '夏色祭簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%A4%8F%E8%89%B2%E7%A5%AD")
    elif text == '赤井心簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E8%B5%A4%E4%BA%95%E5%BF%83")
    elif text == '夜空梅露簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%A4%9C%E7%A9%BA%E6%A2%85%E9%9C%B2")
    elif text == '亞綺．羅森塔爾簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E4%BA%9A%E7%BB%AE%C2%B7%E7%BD%97%E6%A3%AE%E5%A1%94%E5%B0%94")
    elif text == '百鬼綾目簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E7%99%BE%E9%AC%BC%E7%BB%AB%E7%9B%AE")
    elif text == '湊阿庫婭簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%87%91%E9%98%BF%E5%BA%93%E5%A8%85")
    elif text == '紫咲詩音簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E7%B4%AB%E5%92%B2%E8%AF%97%E9%9F%B3")
    elif text == '癒月巧可簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E6%84%88%E6%9C%88%E5%B7%A7%E5%8F%AF")
    elif text == '大空昴簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%A4%A7%E7%A9%BA%E6%98%B4")
    elif text == '貓又小粥簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E7%8C%AB%E5%8F%88%E5%B0%8F%E7%B2%A5")
    elif text == '戌神沁音簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E6%88%8C%E7%A5%9E%E6%B2%81%E9%9F%B3")
    elif text == '大神澪簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%A4%A7%E7%A5%9E%E6%BE%AA")
    elif text == '兔田佩可拉簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%85%94%E7%94%B0%E4%BD%A9%E5%85%8B%E6%8B%89")
    elif text == '寶鐘瑪琳簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%AE%9D%E9%92%9F%E7%8E%9B%E7%90%B3")
    elif text == '潤羽露西亞簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E6%B6%A6%E7%BE%BD%E9%9C%B2%E8%A5%BF%E5%A8%85")
    elif text == '白銀諾艾爾簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E7%99%BD%E9%93%B6%E8%AF%BA%E8%89%BE%E5%B0%94")
    elif text == '不知火芙蕾雅簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E4%B8%8D%E7%9F%A5%E7%81%AB%E8%8A%99%E8%95%BE%E9%9B%85")
    elif text == '角卷綿芽簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E8%A7%92%E5%8D%B7%E7%BB%B5%E8%8A%BD")
    elif text == '桐生可可簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E6%A1%90%E7%94%9F%E5%8F%AF%E5%8F%AF")
    elif text == '天音彼方簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%A4%A9%E9%9F%B3%E5%BD%BC%E6%96%B9")
    elif text == '常闇永遠簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%B8%B8%E6%9A%97%E6%B0%B8%E8%BF%9C")
    elif text == '姬森璐娜簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%A7%AC%E6%A3%AE%E7%92%90%E5%A8%9C")
    elif text == '雪花菈米簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E9%9B%AA%E8%8A%B1%E8%8F%88%E7%B1%B3")
    elif text == '獅白牡丹簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E7%8B%AE%E7%99%BD%E7%89%A1%E4%B8%B9")
    elif text == '桃鈴音音簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E6%A1%83%E9%93%83%E9%9F%B3%E9%9F%B3")
    elif text == '尾丸波爾卡簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E5%B0%BE%E4%B8%B8%E6%B3%A2%E5%B0%94%E5%8D%A1")
    elif text == '魔乃阿蘿耶(卒業)簡介':
        message = TextSendMessage("https://mzh.moegirl.org.cn/%E9%AD%94%E4%B9%83%E9%98%BF%E8%90%9D%E8%80%B6")
    line_bot_api.reply_message(reply_token, message)
    return 'OK'