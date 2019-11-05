import telegram

apiFile = open("/home/pi/server/CAU_Meal_Bot_Telegram_KEY", 'r')
botToken = apiFile.read().rstrip('\n')
apiFile.close()

bot = telegram.Bot(token = botToken)
botUpdates = bot.getUpdates()

for u in botUpdates:
    print(u.message)
