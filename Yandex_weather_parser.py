import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://www.yandex.ru/pogoda/rostov-na-donu?lat=47.201897981989035&lon=39.66847601377369') # Формирует запрос и отправляет на сервер и обратно
print(response) # Если выдает 200, значит библиотека работает и сервер отвечает
soup = BeautifulSoup(response.text, 'lxml') # Хранит исходный код сайта
items = soup.find_all('a', 'link link_theme_normal text forecast-briefly__day-link i-bem') #извекаем необходимую часть html дерева

for day, i in enumerate(items):
  When = i.find('div', 'forecast-briefly__name').text
  Day = i.find('time', 'time forecast-briefly__date').text
  Daytime_temperature = i.find('div', 'temp forecast-briefly__temp forecast-briefly__temp_day').text
  Temperature_at_night= i.find('div', 'temp forecast-briefly__temp forecast-briefly__temp_night').text
  Сondition = i.find('div', 'forecast-briefly__condition').text

  if day == 1: print("Подробный прогноз на следующию неделю:\n")
  elif day == 8: print("Прогноз погоды на месяц (не точный)\n")

  print(f"День: {When}, {Day} \nТемпература днем: {Daytime_temperature}\nТемпература ночью: {Temperature_at_night}\nСостояние: {Сondition}\n")