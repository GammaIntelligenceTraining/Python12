import requests
from bs4 import BeautifulSoup

url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find('tbody').find_all('tr')

results = {}
for row in table:
    results[row.find_all('td')[0].text] = [row.find_all('td')[1], row.find_all('td')[2],
                                           row.find_all('td')[3], row.find_all('td')[4],
                                           row.find_all('td')[5], row.find_all('td')[6],
                                           row.find_all('td')[7], row.find_all('td')[8],
                                           row.find_all('td')[9], row.find_all('td')[10],
                                           row.find_all('td')[11]]


for city, data in results.items():
    print(city)
    print('Õhutemperatuur (°C)')
    print(f'Keskmine ' + str(data[0].text))
    print(f'Max ' + str(data[1].text))
    print(f'Min ' + str(data[2].text))