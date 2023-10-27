# Simple look at the top 5 most active stocks from Yahoo!Finance

import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/most-active'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


table = soup.find('table')
rows = table.find('tbody').find_all('tr')

# Change number in brackets for more results:
for row in rows[:5]:
    stock = row.find('td', {'aria-label': 'Name'}).text
    price = row.find('td', {'aria-label': 'Price (Intraday)'}).text
    change = row.find('td', {'aria-label': 'Change'}).text
    percent = row.find('td', {'aria-label': '% Change'}).text
    
    print(f"Name: {stock}  Price: {price}  Change: {change}  % Change: {percent}")
    