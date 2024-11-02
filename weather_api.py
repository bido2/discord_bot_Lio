import requests

def get_weather_info():
    responce = requests.get(base_url)

    if responce.status_code == 200:
        weather_data = responce.json()
        return weather_data
    else:
        print(f'Failed to retreive data {responce.status_code}')


def return_weather_info(city):
    city+= city.capitalize()
    base_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key=NDPVCQ2HDSXVDQPMYNMHBVVVL&contentType=json'
    weather_info = get_weather_info()

    if weather_info:
        return f'temperatura: {weather_info["days"][0]["temp"]}'