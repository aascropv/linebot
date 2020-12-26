from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, send_template_message_hololive, send_carousel_template_holo_talent, send_carousel_template_holo1st , send_carousel_template_holo2nd, send_carousel_template_holo_gamers, send_carousel_template_holo3rd, send_carousel_template_holo4th, send_carousel_template_holo5th, send_members_message, live_stream_search

import requests
import json

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def hololive_intro(self, event):
        text = event.message.text
        return text == "Hololive"

    def hololive_members_intro(self, event):
        text = event.message.text
        return text == "Hololive member"
    
    def hololive_talent_intro(self, event):
        text = event.message.text
        return text == "HololiveTalent"
    
    def hololive1st_intro(self, event):
        text = event.message.text
        return text == "Hololive1st"

    def hololive2nd_intro(self, event):
        text = event.message.text
        return text == "Hololive2nd"

    def hololive_gamers_intro(self, event):
        text = event.message.text
        return text == "HololiveGamers"

    def hololive3rd_intro(self, event):
        text = event.message.text
        return text == "Hololive3rd"
    
    def hololive4th_intro(self, event):
        text = event.message.text
        return text == "Hololive4th"

    def hololive5th_intro(self, event):
        text = event.message.text
        return text == "Hololive5th"

    def choosing_members(self, event):
        text = event.message.text
        return text[-2:] == "簡介"

    def searching_live_stream(self, event):
        text = event.message.text
        return text[-4:] == "live"

    def on_enter_hololive(self, event):
        print("I'm entering hololive_intro")
        reply_token = event.reply_token
        params = {'channel_id': 9}
        r = requests.get('https://api.holotools.app/v1/live', params=params)
        data_json = json.loads(r.text)
        # send_text_message(reply_token, str(data_json['live']))
        if str(data_json["live"]) == "[]":
            send_text_message(reply_token, "Not streaming")
        else :
            send_text_message(reply_token, "https://www.youtube.com/watch?v=" + data_json["live"][0]['yt_video_key'])
        # send_image_url(reply_token, "https://i.ibb.co/WG7cXHV/hololive.jpg")
        self.go_back()

    def on_exit_hololive(self, event):
        print("Leaving hololive_intro")

    def on_enter_hololive_members(self, event):
        print("I'm entering hololive_members_intro")
        reply_token = event.reply_token
        send_template_message_hololive(reply_token)
        self.go_back(event)

    def on_exit_hololive_members(self, event):
        print("Leaving hololive_members_intro")

    def on_enter_hololive_talent(self, event):
        print("I'm entering hololivetalent")
        reply_token = event.reply_token
        send_carousel_template_holo_talent(reply_token)
        
    
    def on_exit_hololive_talent(self, event):
        print("Leaving hololivetalent")

    def on_enter_hololive1st(self, event):
        print("I'm entering hololive1st")
        reply_token = event.reply_token
        send_carousel_template_holo1st(reply_token)
        
    
    def on_exit_hololive1st(self, event):
        print("Leaving hololive1st")

    def on_enter_hololive2nd(self, event):
        print("I'm entering hololive2nd")
        reply_token = event.reply_token
        send_carousel_template_holo2nd(reply_token)
        
    
    def on_exit_hololive2nd(self, event):
        print("Leaving hololive2nd")

    def on_enter_hololive_gamers(self, event):
        print("I'm entering hololivegamers")
        reply_token = event.reply_token
        send_carousel_template_holo_gamers(reply_token)
        self.advance()
    
    def on_exit_hololive_gamers(self, event):
        print("Leaving hololivegamers")

    def on_enter_hololive3rd(self, event):
        print("I'm entering hololive3rd")
        reply_token = event.reply_token
        send_carousel_template_holo3rd(reply_token)
        

    def on_exit_hololive3rd(self, event):
        print("Leaving hololive3rd")

    def on_enter_hololive4th(self, event):
        print("I'm entering hololive4th")
        reply_token = event.reply_token
        send_carousel_template_holo4th(reply_token)
        

    def on_exit_hololive4th(self, event):
        print("Leaving hololive4th")

    def on_enter_hololive5th(self, event):
        print("I'm entering hololive5th")
        reply_token = event.reply_token
        send_carousel_template_holo5th(reply_token)
        

    def on_exit_hololive5th(self, event):
        print("Leaving hololive5th")

    def on_enter_hololive_members_choosing(self, event):
        print("I'm entering hololive_members_choosing")
        reply_token = event.reply_token
        text = event.message.text
        send_members_message(reply_token, text)
        self.go_back(event)

    def on_exit_hololive_members_choosing(self, event):
        print("Leaving hololive_members_choosing")

    def on_enter_hololive_stream_searching(self, event):
        print("I'm entering hololive_stream_searching")
        reply_token = event.reply_token
        text = event.message.text
        print(text)
        live_stream_search(reply_token, text)
        self.go_back()

    def on_exit_hololive_stream_searching(self, event):
        print("Leaving hololive_stream_searching")