import requests


def weather():
    s_city = "Moscow, RU"  # 524901
    city_id = 0
    appid = "ebef83c01efee4008c8b37a657d30dfe"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
        pass


def weather2(city_id):
    appid = "ebef83c01efee4008c8b37a657d30dfe"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                        params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        conditions = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        city_name = data['name']
        return conditions, temp, temp_min, temp_max, city_name
    except Exception as e:
        print("Exception (weather):", e)
        pass



