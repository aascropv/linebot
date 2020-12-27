
import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_image_url

load_dotenv()

machine = TocMachine(
    states=["user", "fsm", "hololive", "hololive_members", "hololive_talent", "hololive1st", "hololive2nd", "hololive_gamers","hololive3rd", "hololive4th", "hololive5th", "hololive_members_choosing", "hololive_stream_searching"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "fsm",
            "conditions": "show_fsm",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "hololive",
            "conditions": "hololive_intro",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "hololive_members",
            "conditions": "hololive_members_intro",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "hololive_talent",
            "conditions": "hololive_talent_intro",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "hololive1st",
            "conditions": "hololive1st_intro",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "hololive2nd",
            "conditions": "hololive2nd_intro",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "hololive_gamers",
            "conditions": "hololive_gamers_intro",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "hololive3rd",
            "conditions": "hololive3rd_intro",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "hololive4th",
            "conditions": "hololive4th_intro",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "hololive5th",
            "conditions": "hololive5th_intro",
        },
        {
            "trigger": "advance",
            "source": ["hololive_talent", "hololive1st", "hololive2nd", "hololive_gamers", "hololive3rd", "hololive4th", "hololive5th"],
            "dest": "hololive_members_choosing",
            "conditions": "choosing_members",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "hololive_stream_searching",
            "conditions": "searching_live_stream",
        },
        {
            "trigger": "go_back", 
            "source": ["fsm", "hololive", "hololive_members",  "hololive_members_choosing", "hololive_stream_searching"], 
            "dest": "user"
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


# @app.route("/callback", methods=["POST"])
# def callback():
#     signature = request.headers["X-Line-Signature"]
#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # parse webhook body
#     try:
#         events = parser.parse(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     # if event is MessageEvent and message is TextMessage, then echo text
#     for event in events:
#         if not isinstance(event, MessageEvent):
#             continue
#         if not isinstance(event.message, TextMessage):
#             continue

#         line_bot_api.reply_message(
#             event.reply_token, TextSendMessage(text=event.message.text)
#         )

#     return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")
        print(f"\nFSM STATE: {machine.state}")

    return "OK"

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)