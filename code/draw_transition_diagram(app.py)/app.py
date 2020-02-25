#ngrok http 8000
#python3 app.py
#copy the file in textfile can draw the figure you want
######################################header file########################################
import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message
########################################################################################
load_dotenv()
#10/38 20/38 8/28
machine = TocMachine(
    states=['0',"2","4","6","8","10","12","14","16","18","20","22","24","26","28","30"],
    transitions=[
        #state 0
        {"trigger":"","source": "0","dest": "0","conditions": "1",},
        {"trigger":"","source": "0","dest": "2","conditions": "0",},
        #state 2
        {"trigger":"","source": "2","dest": "0","conditions": "10/38",},
        {"trigger":"","source": "2","dest": "2","conditions": "20/38",},
        {"trigger":"","source": "2","dest": "4","conditions": "8/38",},
        #state 4
        {"trigger":"","source": "4","dest": "2","conditions": "10/38",},
        {"trigger":"","source": "4","dest": "4","conditions": "20/38",},
        {"trigger":"","source": "4","dest": "6","conditions": "8/38",},
        #state 6
        {"trigger":"","source": "6","dest": "4","conditions": "10/38",},
        {"trigger":"","source": "6","dest": "6","conditions": "20/38",},
        {"trigger":"","source": "6","dest": "8","conditions": "8/38",},
        #state 8
        {"trigger":"","source": "8","dest": "6","conditions": "10/38",},
        {"trigger":"","source": "8","dest": "8","conditions": "20/38",},
        {"trigger":"","source": "8","dest": "10","conditions": "8/38",},
        #state 10
        {"trigger":"","source": "10","dest": "8","conditions": "10/38",},
        {"trigger":"","source": "10","dest": "10","conditions": "20/38",},
        {"trigger":"","source": "10","dest": "12","conditions": "8/38",},
        #state 12
        {"trigger":"","source": "12","dest": "10","conditions": "10/38",},
        {"trigger":"","source": "12","dest": "12","conditions": "20/38",},
        {"trigger":"","source": "12","dest": "14","conditions": "8/38",},
        #state 14
        {"trigger":"","source": "14","dest": "12","conditions": "10/38",},
        {"trigger":"","source": "14","dest": "14","conditions": "20/38",},
        {"trigger":"","source": "14","dest": "16","conditions": "8/38",},
        #state 16
        {"trigger":"","source": "16","dest": "14","conditions": "10/38",},
        {"trigger":"","source": "16","dest": "16","conditions": "20/38",},
        {"trigger":"","source": "16","dest": "18","conditions": "8/38",},
        #state 18
        {"trigger":"","source": "18","dest": "16","conditions": "10/38",},
        {"trigger":"","source": "18","dest": "18","conditions": "20/38",},
        {"trigger":"","source": "18","dest": "20","conditions": "8/38",},
        #state 20
        {"trigger":"","source": "20","dest": "18","conditions": "10/38",},
        {"trigger":"","source": "20","dest": "20","conditions": "20/38",},
        {"trigger":"","source": "20","dest": "22","conditions": "8/38",},
        #state 22
        {"trigger":"","source": "22","dest": "20","conditions": "10/38",},
        {"trigger":"","source": "22","dest": "22","conditions": "20/38",},
        {"trigger":"","source": "22","dest": "24","conditions": "8/38",},
        #state 24
        {"trigger":"","source": "24","dest": "22","conditions": "10/38",},
        {"trigger":"","source": "24","dest": "24","conditions": "20/38",},
        {"trigger":"","source": "24","dest": "26","conditions": "8/38",},
        #state 26
        {"trigger":"","source": "26","dest": "24","conditions": "10/38",},
        {"trigger":"","source": "26","dest": "26","conditions": "20/38",},
        {"trigger":"","source": "26","dest": "28","conditions": "8/38",},
        #state 28
        {"trigger":"","source": "28","dest": "26","conditions": "10/38",},
        {"trigger":"","source": "28","dest": "28","conditions": "20/38",},
        {"trigger":"","source": "28","dest": "30","conditions": "8/38",},
        #state 30
        {"trigger":"","source": "30","dest": "30","conditions": "1",},
    ],
    initial="10",
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


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

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

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)#parse the recvmsg to lowercase 
    except InvalidSignatureError:
        abort(400)

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
