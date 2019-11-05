import sys
import ChatBotModel

def proc_303_lunch(bot, update):
    db = open("/home/pi/serverDB/303_lunch", 'r')
    cauMealBot.sendMessage(db.read())
    db.close()

def proc_303_dinner(bot, update):
    db = open("/home/pi/serverDB/303_dinner", 'r')
    cauMealBot.sendMessage(db.read())
    db.close() 

def proc_308_breakfast(bot, update):
    db = open("/home/pi/serverDB/308_breakfast", 'r')
    cauMealBot.sendMessage(db.read())
    db.close()

def proc_308_lunch(bot, update):
    db = open("/home/pi/serverDB/308_lunch", 'r')
    cauMealBot.sendMessage(db.read())
    db.close()

def proc_308_dinner(bot, update):
    db = open("/home/pi/serverDB/308_dinner", 'r')
    cauMealBot.sendMessage(db.read())
    db.close()

def proc_309_lunch(bot, update):
    db = open("/home/pi/serverDB/309_lunch", 'r')
    cauMealBot.sendMessage(db.read())
    db.close()

def proc_309_dinner(bot, update):
    db = open("/home/pi/serverDB/309_dinner", 'r')
    cauMealBot.sendMessage(db.read())
    db.close()

def proc_310_breakfast(bot, update):
    db = open("/home/pi/serverDB/310_breakfast", 'r')
    cauMealBot.sendMessage(db.read())
    db.close()

def proc_310_lunch(bot, update):
    db = open("/home/pi/serverDB/310_lunch", 'r')
    cauMealBot.sendMessage(db.read())
    db.close()

def proc_310_dinner(bot, update):
    db = open("/home/pi/serverDB/310_dinner", 'r')
    cauMealBot.sendMessage(db.read())
    db.close()

def proc_cecom(bot, update):
    cauMealBot.sendMessage('대학인의 글쓰기를 수강하며 학습한 내용으로 10점급의 리뷰, 페이스북 페이지 \'망했어요\'와 \'언더케이지\' 우수 참여자를 달성하셨지만 \'우매하다\'의 뜻은 모르고, 인생을 루팅한 뒤 데자와에 밥을 말아먹으며 코딩 경험을 쌓아 젊은 개발자로서 유튜브에 앱 리뷰를 쟁취하고 가스버너를 뜯어 미니PC를 만들며 병역이 당당한 나라를 위해 병무청 병역판정 신체검사에서 신체등위 2급을 쟁취하였고, 인생의 잘못된 선택인 대학원을 고민하면서도 스트라다라는 맛있는 카페가 있는 의대 건물 따위는 포탈로 활용하고, 정작 카우대 바로 앞 이디야 두고 \'ㅅㅑ 입구 이디야\'와 \'신림 또리스\'를 애용하는 따뜻한 관악과 행복한 변화 사람사는 동작이 내세우는 그는  LG와 유현욱 선배님를 휘어잡고 서울특별시 동작구 흑석로 84 107관 408호를 영토로 하는 세콤의 황제, 성보의 자랑 중앙의 보배, 이 시대 의혈의 아들 (펄ー럭) 썬 오브 카우 애국소프트 나라사랑소프트 유ー즈풀 \'황제\' 유.용.민')

cauMealBot = ChatBotModel.CAUMealBot()
cauMealBot.add_handler('303Lunch', proc_303_lunch)
cauMealBot.add_handler('303Dinner', proc_303_dinner)
cauMealBot.add_handler('308Breakfast', proc_308_breakfast)
cauMealBot.add_handler('CECOM', proc_cecom)
cauMealBot.start()
