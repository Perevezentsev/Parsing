import requests
import json


origin = input('Введите город отправления:').capitalize()
destination = input('Введите город назначения:').capitalize()


def iata_code(city):
    iata = requests.get('http://api.travelpayouts.com/data/ru/cities.json')
    data = json.loads(iata.text)

    for i in range(len(data)):
        if data[i]['name'] == city:
            city_code = data[i]['code']
            break
    return city_code


def min_price(origin, destination):
    req = requests.get("http://min-prices.aviasales.ru/calendar_preload?origin=" + iata_code(origin) + "&destination=" +
                       iata_code(destination)+"&one_way=true")
    data = json.loads(req.text)
    best_prices = data['best_prices'][0]

    return best_prices


actual_min_price = min_price(origin, destination)

print('Город вылета:', origin, '\n'
      'Пункт назначения:', destination, '\n' 
      'Дата вылета:', actual_min_price['depart_date'], '\n'
      'Цена билета:', actual_min_price['value'])

