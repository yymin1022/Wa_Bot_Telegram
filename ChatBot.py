import logging
import random
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
    strInput = update.message.text

    if sendMenuMessage(strInput) != "None":
        context.bot.send_message(chat_id=update.effective_chat.it, text=sendMenuMessage(strInput))
    elif sendWaMessage(strInput) != "None":
        context.bot.send_message(chat_id=update.effective_chat.it, text=sendWaMessage(strInput))

def sendMenuMessage(message):
    if ("303" in update.message.text) and (("중식" in update.message.text) or ("점심" in update.message.text)):
        db = open("/home/pi/serverDB/303_lunch", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("303" in update.message.text) and (("석식" in update.message.text) or ("저녁" in update.message.text)):
        db = open("/home/pi/serverDB/303_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("308" in update.message.text) and (("조식" in update.message.text) or ("아침" in update.message.text)):
        db = open("/home/pi/serverDB/308_breakfast", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("308" in update.message.text) and (("중식" in update.message.text) or ("점심" in update.message.text)):
        db = open("/home/pi/serverDB/308_lunch", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("308" in update.message.text) and (("석식" in update.message.text) or ("저녁" in update.message.text)):
        db = open("/home/pi/serverDB/308_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("309" in update.message.text) and (("중식" in update.message.text) or ("점심" in update.message.text)):
        db = open("/home/pi/serverDB/309_lunch", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("309" in update.message.text) and (("석식" in update.message.text) or ("저녁" in update.message.text)):
        db = open("/home/pi/serverDB/309_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("310" in update.message.text) and (("조식" in update.message.text) or ("아침" in update.message.text)):
        db = open("/home/pi/serverDB/310_breakfast", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("310" in update.message.text) and (("중식" in update.message.text) or ("점심" in update.message.text)):
        db = open("/home/pi/serverDB/310_lunch", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    if ("310" in update.message.text) and (("석식" in update.message.text) or ("저녁" in update.message.text)):
        db = open("/home/pi/serverDB/310_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
        
def sendWaMessage(update, context):
    if "와.." in update.message.text:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "갑부;;")

messageHandler = MessageHandler(Filters.text, sendMessage)
dispatcher.add_handler(messageHandler)
