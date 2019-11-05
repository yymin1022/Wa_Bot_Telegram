import logging
import telegram
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler, Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

apiKeyFile = open("/home/pi/server/CAU_Meal_Bot_Telegram_KEY", 'r')
TOKEN = apiKeyFile.read().rstrip('\n')
apiKeyFile.close()

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, World!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

def sendMenuMessage(update, context):
    if "303 중식" in update.message.text:
        db = open("/home/pi/serverDB/303_lunch", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    elif "303 석식" in update.message.text:
        db = open("/home/pi/serverDB/303_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    elif "308 조식" in update.message.text:
        db = open("/home/pi/serverDB/308_breakfast", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    elif "308 중식" in update.message.text:
        db = open("/home/pi/serverDB/308_lunch", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    elif "308 석식" in update.message.text:
        db = open("/home/pi/serverDB/308_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    elif "309 중식" in update.message.text:
        db = open("/home/pi/serverDB/309_lunch", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    elif "309 석식" in update.message.text:
        db = open("/home/pi/serverDB/309_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    elif "310 조식" in update.message.text:
        db = open("/home/pi/serverDB/310_breakfast", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    elif "310 중식" in update.message.text:
        db = open("/home/pi/serverDB/310_lunch", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()
    elif "310 석식" in update.message.text:
        db = open("/home/pi/serverDB/310_dinner", 'r')
        context.bot.send_message(chat_id = update.effective_chat.id, text = db.read())
        db.close()

message_handler = MessageHandler(Filters.text, sendMenuMessage)
dispatcher.add_handler(message_handler)
