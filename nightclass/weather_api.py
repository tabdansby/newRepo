"""put in location, get back current temp; ask user if they want temp in C or F;
advanced: get 3-5 day forecast"""

import requests
import time

zip_code = input('What is your zip code?: ')
payload = {'appid': 'a7b7bd116544e6dc7c390e5f366502d3', 'zip': zip_code}
r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)

data = r.json()
# temps = data['main']['temp']

temperature_preference = input('Do you want the temperature in Fahrenheit or Celsius?: ')
f = int((9/5) * (data['main']['temp'] - 273) + 32)
c = int(data['main']['temp'] - 273)

if temperature_preference == 'Fahrenheit':
    print(f)
else:
    print(c)

forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=payload)
forecast_info = forecast.json()

print(forecast_info['list']['main']['temp'])

#print (data['main']['temp'])

#print(forecast.url)
#print(data['main']['temp']['name'][])

#<---this is a requests method; check it out in python docs
