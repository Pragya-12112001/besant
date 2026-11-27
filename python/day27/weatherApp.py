import requests

api_key = 'c5921848b36309b44b74f718e58b9f3e'

city = input('enter city name: ')
url = 'https://api.openweathermap.org/data/2.5/weather'

params = {
  'q': city,
  'appid': api_key,
  'units': 'metric'
}

res = requests.get(url, params=params)
data = res.json()
print(data)
if res.status_code == 200:
  print(f'city: {data['name']}')
  print(f'temp: {data['main']['temp']} C')
  print(f'humidity: {data['main']['humidity']}%')
  print(f'weather: {data['weather'][0]['description']}')
else:
  print('unable to recieve weather information')
  print(data.get('message'))
