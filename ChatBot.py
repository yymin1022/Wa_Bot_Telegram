import sys
import ChatBotModel

def proc_breakfast(bot, update):
    cauMealBot.sendMessage('Breakfast')

def proc_lunch(bot, update):
    cauMealBot.sendMessage('Lunch')

def proc_dinner(bot, update):
    cauMealBot.sendMessage('Dinner')

cauMealBot = ChatBotModel.CAUMealBot()
cauMealBot.add_handler('Breakfast', proc_breakfast)
cauMealBot.add_handler('Lunch', proc_lunch)
cauMealBot.add_handler('Dinner', proc_dinner)
cauMealBot.start()
