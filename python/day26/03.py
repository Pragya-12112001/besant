import requests
from bs4 import BeautifulSoup

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
  'title': 'python programming',
  'body': 'learning networking',
  'userId': 1
}

response = requests.post(url, json=data)

res = response.json()
print(res)

print(f'title: {res['title']}')
print(f'body: {res['body']}')
print(f'userID: {res['userId']}')
print(f'ID: {res['id']}')