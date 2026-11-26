import requests
from bs4 import BeautifulSoup

url = 'https://dummyjson.com/quotes/200'

response = requests.get(url)
data = response.json()

print(data['quote'])
print(data['author'])