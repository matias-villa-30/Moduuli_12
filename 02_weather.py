import requests

city_name = input("Please enter a city name: ")
api_key = "a0f9067e46355b253baf763ee7ed8422"

api = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name.lower()}&appid={api_key}"


response = requests.get(api).json()

if response:
    latitud = response[0]['lat']
    longitud = response[0]['lon']
    temperatura_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={api_key}"
    temperatura = requests.get(temperatura_api).json()
    temp_kelvin = temperatura["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15
    print(f"Temperature in {city_name.title()} is {temp_celsius:.1f} degrees Celsius.")

else:
    print("City not found")
