import requests
from bs4 import BeautifulSoup as BS

h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

eur_yen_link = 'https://www.google.com/search?q=yen+to+eur&sxsrf=AB5stBjPGKf7am73btfFgSn_VadxOXVgPQ%3A1690391418441&ei=elPBZOO2GtmGxc8PurScqAU&ved=0ahUKEwjj25vg7qyAAxVZQ_EDHToaB1UQ4dUDCA8&uact=5&oq=yen+to+eur&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnllbiB0byBldXIyDBAAGIoFGEMYRhiCAjIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjRFlAAWIwVcAF4AZABAJgB8QGgAeoNqgEGMC4xMC4xuAEDyAEA-AEBwgIEECMYJ8ICBxAjGIoFGCfCAgcQABiKBRhDwgINEC4YigUYxwEY0QMYQ8ICBRAuGIAEwgILEC4YgAQYxwEY0QPCAgcQABiABBgK4gMEGAAgQYgGAQ&sclient=gws-wiz-serp'
usd_sek_link = 'https://www.google.com/search?q=usd+to+sek&sxsrf=AB5stBjLsjYIcKv5NIQ63HmaiG7BmoiR5A%3A1690391426479&ei=glPBZK_qHO2Hxc8PkryLUA&ved=0ahUKEwivs4bk7qyAAxXtQ_EDHRLeAgoQ4dUDCA8&uact=5&oq=usd+to+sek&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnVzZCB0byBzZWsyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESL4eUABYlRxwA3gBkAEAmAHVAaABoBCqAQYwLjEyLjG4AQPIAQD4AQHCAgcQABiKBRhDwgILEC4YgAQYxwEY0QPCAgUQLhiABMICBxAjGIoFGCfCAgcQABiABBgK4gMEGAAgQYgGAQ&sclient=gws-wiz-serp'

r = requests.get(eur_yen_link, headers=h)
soup = BS(r.content, 'html.parser')
match = soup.find('span', class_='DFlfde SwHCTb')
# exchange_rate = float(match.text.replace(',', '.'))
exchange_rate = float(match['data-value'])
user_sum = float(input('Please enter amount in YEN: '))
print(user_sum * exchange_rate, 'EUR')

user_sum = float(input('Please enter amount in EUR: '))
print(user_sum / exchange_rate, 'YEN')


r = requests.get(usd_sek_link, headers=h)
soup = BS(r.content, 'html.parser')
match = soup.find('span', class_='DFlfde SwHCTb')
# exchange_rate = float(match.text.replace(',', '.'))
exchange_rate = float(match['data-value'])
user_sum = float(input('Please enter amount in USD: '))
print(user_sum * exchange_rate, 'SEK')

user_sum = float(input('Please enter amount in SEK: '))
print(user_sum / exchange_rate, 'USD')
