import json
import logging
import random
import requests
import telegram
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler, Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

apiKeyFile = open("/home/server/CAU_Meal_Bot_Telegram_KEY", 'r')
TOKEN = apiKeyFile.read().rstrip('\n')
apiKeyFile.close()

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
    resultData = requests.post("https://wa-api.defcon.or.kr/getMessage", json=requestData).json()

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
