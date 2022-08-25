from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler, Updater
import telegram

import json
import os
import random
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN", "NO_TOKEN")
WA_URL = os.getenv("WA_API_SERVER", "localhost:8080")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="와.. 역시;;")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

def sendMessage(update, context):
    sendWaMessage(update.message.text, update, context)

def sendWaMessage(message, update, context):
    requestData = dict([("msg", message), ("room", update.effective_chat.id), ("sender", update.effective_chat.id)])
    resultData = requests.post(WA_API_SERVER, json=requestData).json()

    resultMessage = resultData["DATA"]["msg"]

    if resultData["RESULT"]["RESULT_CODE"] == 0:
        if resultMessage.find("\\m") > 0:
            resultMessageList = resultMessage.split("\\m")

            for resultMessageItem in resultMessageList:
                context.bot.send_message(chat_id=update.effective_chat.id, text=resultMessageItem)
        else:
            resultMessage = resultMessage.replace("\\n", "\n")
            context.bot.send_message(chat_id=update.effective_chat.id, text=resultMessage)

messageHandler = MessageHandler(Filters.text, sendMessage)
dispatcher.add_handler(messageHandler)
