import logging
import random
import telegram
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler, Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

apiKeyFile = open("/home/yong/server/CAU_Meal_Bot_Telegram_KEY", 'r')
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

    if("ㅋ" in update.message.text):
        text = update.message.text
        num = text.count("ㅋ")
        num += text.count("ㅌ")
        num += text.count("ㄱ")
        num += text.count("ㄲ")
        num += text.count("ㄴ")
        num += text.count("ㅎ")
        if num >= 5:
            context.bot.send_message(chat_id = update.effective_chat.id, text = "뭘 웃어요;")
    
    if ("헐.." in update.message.text):
        strMessage = "쉽덕;;"
        context.bot.send_message(chat_id = update.effective_chat.id, text = strMessage)

    if ("아.." in update.message.text):
        num = random.randrange(1, 5)
        if num == 1:
            strMessage = "그렇군요..."
        if num == 2:
            strMessage = "글쿤.."
        if num == 3:
            strMessage = "그래요.."
        if num == 4:
            strMessage = "좋네요.."
        context.bot.send_message(chat_id = update.effective_chat.id, text = strMessage)

    if ("이런.." in update.message.text):
        num = random.randrange(1, 3)
        if num == 1:
            strMessage = "안타깝군요.."
        if num == 2:
            strMessage = "안됐군요.."
        context.bot.send_message(chat_id = update.effective_chat.id, text = strMessage)

    if ("와.." in update.message.text) or ("와;;" in update.message.text):
        num = random.randrange(1, 6)
        if num == 1:
            strMessage = "갑부.."
        if num == 2:
            strMessage = "마스터.."
        if num == 3:
            strMessage = "역시.."
        if num == 4:
            strMessage = "인싸.."
        if num == 5:
            strMessage = "기만;;"
        context.bot.send_message(chat_id = update.effective_chat.id, text = strMessage)
    if ("와!" in update.message.text):
        context.bot.send_message(chat_id = update.effective_chat.id, text = "샌즈!")
        context.bot.send_message(chat_id = update.effective_chat.id, text = "아시는구나!")
        context.bot.send_message(chat_id = update.effective_chat.id, text = "겁.나.어.렵.습.니.다.")

message_handler = MessageHandler(Filters.text, sendMenuMessage)
dispatcher.add_handler(message_handler)
