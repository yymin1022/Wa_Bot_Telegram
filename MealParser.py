from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

str303Lunch = ""
str303Dinner = ""
str308Breakfast = ""
str308Lunch = ""
str308Dinner = ""
str309Lunch = ""
str309Dinner = ""
str310Breakfast = ""
str310Lunch = ""
str310Dinner = ""

url303 = "https://bds.bablabs.com/restaurants/LTIzODAwOTc1?campus_id=biV2tiK41v"
url308 = "https://bds.bablabs.com/restaurants/LTIzODA3NTM2?campus_id=biV2tiK41v"
url309 = "https://bds.bablabs.com/restaurants/MjIzMDk0MDAx?campus_id=biV2tiK41v"
url310 = "https://bds.bablabs.com/restaurants/MjMyNjY2NzA0?campus_id=biV2tiK41v"

html = urlopen(url303).read()
soup = BeautifulSoup(html, "html.parser")
div_today = soup.find("div", class_="date-wrapper")
div_lunch = div_today.find_all("div", class_= "label-wrapper")[0]
div_dinner = div_today.find_all("div", class_= "label-wrapper")[1]

for divs in div_lunch.find_all("div", class_= "card card-menu"):
    str303Lunch = str303Lunch + divs.find("div", class_="card-text").text + "\n"
for divs in div_dinner.find_all("div", class_= "card card-menu"):
    str303Dinner = str303Dinner + divs.find("div", class_="card-text").text + "\n"
    
file303Lunch = open("/home/pi/serverDB/303_lunch", 'w')
file303Lunch.write(str303Lunch)
file303Lunch.close()
file303Dinner = open("/home/pi/serverDB/303_dinner", 'w')
file303Dinner.write(str303Dinner)
file303Dinner.close()
    
html = urlopen(url308).read()
soup = BeautifulSoup(html, "html.parser")
div_today = soup.find("div", class_="date-wrapper")
div_breakfast = div_today.find_all("div", class_= "label-wrapper")[0]
div_lunch = div_today.find_all("div", class_= "label-wrapper")[1]
div_dinner = div_today.find_all("div", class_= "label-wrapper")[2]

for divs in div_breakfast.find_all("div", class_= "card card-menu"):
    str308Breakfast = str308Breakfast + divs.find("div", class_="card-text").text + "\n"
for divs in div_lunch.find_all("div", class_= "card card-menu"):
    str308Lunch = str308Lunch + divs.find("div", class_="card-text").text + "\n"
for divs in div_dinner.find_all("div", class_= "card card-menu"):
    str308Dinner = str308Dinner + divs.find("div", class_="card-text").text + "\n"
    
file308Breakfast = open("/home/pi/serverDB/308_breakfast", 'w')
file308Breakfast.write(str308Breakfast)
file308Breakfast.close()
file308Lunch = open("/home/pi/serverDB/308_lunch", 'w')
file308Lunch.write(str308Lunch)
file308Lunch.close()
file308Dinner = open("/home/pi/serverDB/308_dinner", 'w')
file308Dinner.write(str308Dinner)
file308Dinner.close()
    
html = urlopen(url309).read()
soup = BeautifulSoup(html, "html.parser")
div_today = soup.find("div", class_="date-wrapper")
div_lunch = div_today.find_all("div", class_= "label-wrapper")[0]
div_dinner = div_today.find_all("div", class_= "label-wrapper")[1]

for divs in div_lunch.find_all("div", class_= "card card-menu"):
    str309Lunch = str309Lunch + divs.find("div", class_="card-text").text + "\n"
for divs in div_dinner.find_all("div", class_= "card card-menu"):
    str309Dinner = str309Dinner + divs.find("div", class_="card-text").text + "\n"
    
file309Lunch = open("/home/pi/serverDB/309_lunch", 'w')
file309Lunch.write(str309Lunch)
file309Lunch.close()
file309Dinner = open("/home/pi/serverDB/309_dinner", 'w')
file309Dinner.write(str309Dinner)
file309Dinner.close()
    
html = urlopen(url310).read()
soup = BeautifulSoup(html, "html.parser")
div_today = soup.find("div", class_="date-wrapper")
div_breakfast = div_today.find_all("div", class_= "label-wrapper")[0]
div_lunch = div_today.find_all("div", class_= "label-wrapper")[1]
div_dinner = div_today.find_all("div", class_= "label-wrapper")[2]

for divs in div_breakfast.find_all("div", class_= "card card-menu"):
    str310Breakfast = str310Breakfast + divs.find("div", class_="card-text").text + "\n"
for divs in div_lunch.find_all("div", class_= "card card-menu"):
    str310Lunch = str310Lunch + divs.find("div", class_="card-text").text + "\n"
for divs in div_dinner.find_all("div", class_= "card card-menu"):
    str310Dinner = str310Dinner + divs.find("div", class_="card-text").text + "\n"
    
file310Breakfast = open("/home/pi/serverDB/310_breakfast", 'w')
file310Breakfast.write(str310Dinner)
file310Breakfast.close()
file310Lunch = open("/home/pi/serverDB/310_lunch", 'w')
file310Lunch.write(str310Lunch)
file310Lunch.close()
file310Dinner = open("/home/pi/serverDB/310_dinner", 'w')
file310Dinner.write(str310Dinner)
file310Dinner.close()