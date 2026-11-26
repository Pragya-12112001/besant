import requests
from bs4 import BeautifulSoup

url = 'https://youtube.com'
headers = {
  'user-agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

if soup.title:
  print(f'website title: {soup.title.get_text(strip=True)}')
  print(f'status code: {response.status_code}')
else:
  print('title not found')
  print(f'status code: {response.status_code}')
# print(soup.prettify())