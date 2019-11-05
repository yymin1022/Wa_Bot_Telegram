import telegram
from telegram.ext import Updater, CommandHandler

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 0
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.core.getUpdates()[-1].message.chat.id, text=text)
        print(self.core.getUpdates()[-1].message.chat.id)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class CAUMealBot(TelegramBot):
    def __init__(self):
        apiKeyFile = open("/home/pi/server/CAU_Meal_Bot_Telegram_KEY", 'r')
        self.token = apiKeyFile.read().rstrip('\n')
        apiKeyFile.close()

        TelegramBot.__init__(self, 'CAU Meal Bot', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.updater.start_polling()
        self.updater.idle()
