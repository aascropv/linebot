from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, send_template_message_hololive, send_carousel_template_holo_talent, send_carousel_template_holo1st , send_carousel_template_holo2nd, send_carousel_template_holo_gamers, send_carousel_template_holo3rd, send_carousel_template_holo4th, send_carousel_template_holo5th


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

    def on_enter_hololive(self, event):
        print("I'm entering hololive_intro")
        reply_token = event.reply_token
        send_image_url(reply_token, "https://i.ibb.co/WG7cXHV/hololive.jpg")
        self.go_back()

    def on_exit_hololive(self):
        print("Leaving hololive_intro")

    def on_enter_hololive_members(self, event):
        print("I'm entering hololive_members_intro")
        reply_token = event.reply_token
        send_template_message_hololive(reply_token)
        self.advance()
        # self.go_back()

    def on_exit_hololive_members(self, event):
        print("Leaving hololive_members_intro")

    def on_enter_hololive_talent(self, event):
        print("I'm entering hololivetalent")
        reply_token = event.reply_token
        send_carousel_template_holo_talent(reply_token)
        self.go_back()
    
    def on_exit_hololive_talent(self):
        print("Leaving hololivetalent")

    def on_enter_hololive1st(self, event):
        print("I'm entering hololive1st")
        reply_token = event.reply_token
        send_carousel_template_holo1st(reply_token)
        self.go_back()
    
    def on_exit_hololive1st(self):
        print("Leaving hololive1st")

    def on_enter_hololive2nd(self, event):
        print("I'm entering hololive2nd")
        reply_token = event.reply_token
        send_carousel_template_holo2nd(reply_token)
        self.go_back()
    
    def on_exit_hololive2nd(self):
        print("Leaving hololive2nd")

    def on_enter_hololive_gamers(self, event):
        print("I'm entering hololivegamers")
        reply_token = event.reply_token
        send_carousel_template_holo_gamers(reply_token)
        self.go_back()
    
    def on_exit_hololive_gamers(self):
        print("Leaving hololivegamers")

    def on_enter_hololive3rd(self, event):
        print("I'm entering hololive3rd")
        reply_token = event.reply_token
        send_carousel_template_holo3rd(reply_token)
        self.go_back()

    def on_exit_hololive3rd(self):
        print("Leaving hololive3rd")

    def on_enter_hololive4th(self, event):
        print("I'm entering hololive4th")
        reply_token = event.reply_token
        send_carousel_template_holo4th(reply_token)
        self.go_back()

    def on_exit_hololive4th(self):
        print("Leaving hololive4th")

    def on_enter_hololive5th(self, event):
        print("I'm entering hololive5th")
        reply_token = event.reply_token
        send_carousel_template_holo5th(reply_token)
        self.go_back()

    def on_exit_hololive5th(self):
        print("Leaving hololive5th")