import requests

def get_weather_forecast(city, api_key='67adb7c42845b6f3d4cae85a355e57c3'):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    r = requests.get(url)
    content = r.json()
    # print(content['list'])

    with open('weather_data.txt', 'a') as file:
        for i in content['list']:
            file.write(f"{city}, {i['dt_txt']}, {i['main']['temp']}, {i['weather'][0]['description']}\n")


get_weather_forecast(city='Aleppo')