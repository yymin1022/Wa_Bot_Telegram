from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update

import json
import os
import random
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN", "NO_TOKEN")
WA_API_SERVER = os.getenv("WA_API_SERVER", "localhost:8080")

async def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="와.. 역시;;")

async def sendMessage(update, context):
    sendWaMessage(update.message.text, update, context)

async def sendWaMessage(message, update, context):
    requestData = dict([("msg", message), ("room", str(update.effective_chat.id)), ("sender", update.effective_chat.id)])
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

def main():
    application = Application.builder().token(TOKEN).build()

    messageHandler = MessageHandler(filters.TEXT, sendMessage)
    application.add_handler(messageHandler)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()