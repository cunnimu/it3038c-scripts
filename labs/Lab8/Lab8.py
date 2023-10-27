# Simple look at the top 5 most active stocks from Yahoo!Finance

# Output will look something like this:
# Name: Ford Motor Company  Price: 9.96  Change: -1.39  % Change: -12.25%
# Name: Amazon.com, Inc.  Price: 127.74  Change: +8.17  % Change: +6.83%
# Name: Tesla, Inc.  Price: 207.30  Change: +1.54  % Change: +0.75%
# Name: Intel Corporation  Price: 35.54  Change: +3.02  % Change: +9.29%
# Name: Bank of America Corporation  Price: 25.17  Change: -0.95  % Change: -3.64%

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
    
