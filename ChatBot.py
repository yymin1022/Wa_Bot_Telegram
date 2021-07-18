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
    if "ㄹㅇㅋㅋ" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="ㄹㅇㅋㅋ")
    if "멈춰" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="멈춰!!")
    if "무야호" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="그만큼 신나신다는거지~")
    if "아.." in message:
        randInt = random.randrange(0, 5)
        messageStr = ""

        if randInt == 0:
            messageStr = "글쿤.."
        elif randInt == 1:
            messageStr = "그래요.."
        elif randInt == 2:
            messageStr = "그렇군요.."
        elif randInt == 3:
            messageStr = "안돼.."
        elif randInt == 4:
            messageStr = "메리카노.."
        
        context.bot.send_message(chat_id=update.effective_chat.id, text=messageStr)
    if "와.." in message:
        randInt = random.randrange(0, 5)
        messageStr = ""

        if randInt == 0:
            messageStr = "갑부;;"
        elif randInt == 1:
            messageStr = "기만;;"
        elif randInt == 2:
            messageStr = "ㄹㅇ;;"
        elif randInt == 3:
            messageStr = "마스터;;"
        elif randInt == 4:
            messageStr = "역시;;"
        
        context.bot.send_message(chat_id=update.effective_chat.id, text=messageStr)
    if "와!" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="샌즈!")
        context.bot.send_message(chat_id=update.effective_chat.id, text="아시는구나!")
        context.bot.send_message(chat_id=update.effective_chat.id, text="이거 겁.나.어.렵.습.니.다.")
    if "이런.." in message:
        randInt = random.randrange(0, 2)
        messageStr = ""

        if randInt == 0:
            messageStr = "안됐군요.."
        elif randInt == 1:
            messageStr = "안타깝네요.."
        
        context.bot.send_message(chat_id=update.effective_chat.id, text=messageStr)
    if "자라" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="전기요금아깝다;;")
    if "자야" in message or "개발해야" in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="구라ㅡㅡ;;")
    if "하.." in message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="코딩하기 싫다..")

messageHandler = MessageHandler(Filters.text, sendMessage)
dispatcher.add_handler(messageHandler)
