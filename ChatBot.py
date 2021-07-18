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
    sendMenuMessage(update.message.text, update, context)
    sendWaMessage(update.message.text, update, context)

def sendMenuMessage(message, update, context):
    if ("303" in message) and (("중식" in message) or ("점심" in message)):
        db = open("/home/pi/serverDB/303_lunch", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("303" in message) and (("석식" in message) or ("저녁" in message)):
        db = open("/home/pi/serverDB/303_dinner", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("308" in message) and (("조식" in message) or ("아침" in message)):
        db = open("/home/pi/serverDB/308_breakfast", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("308" in message) and (("중식" in message) or ("점심" in message)):
        db = open("/home/pi/serverDB/308_lunch", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("308" in message) and (("석식" in message) or ("저녁" in message)):
        db = open("/home/pi/serverDB/308_dinner", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("309" in message) and (("중식" in message) or ("점심" in message)):
        db = open("/home/pi/serverDB/309_lunch", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("309" in message) and (("석식" in message) or ("저녁" in message)):
        db = open("/home/pi/serverDB/309_dinner", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("310" in message) and (("조식" in message) or ("아침" in message)):
        db = open("/home/pi/serverDB/310_breakfast", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("310" in message) and (("중식" in message) or ("점심" in message)):
        db = open("/home/pi/serverDB/310_lunch", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
    if ("310" in message) and (("석식" in message) or ("저녁" in message)):
        db = open("/home/pi/serverDB/310_dinner", 'r')
        context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())
        db.close()
        
def sendWaMessage(message, update, context):
    if "와.." in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="갑부;;")
    if "와!" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="샌즈!")
        context.bot.send_message(chat_id=update.effective_chat.id, text="아시는구나!")
        context.bot.send_message(chat_id=update.effective_chat.id, text="이거 겁.나.어.렵.습.니.다.")
    if "자야" in message or "개발해야" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="구라ㅡㅡ;;")

messageHandler = MessageHandler(Filters.text, sendMessage)
dispatcher.add_handler(messageHandler)
