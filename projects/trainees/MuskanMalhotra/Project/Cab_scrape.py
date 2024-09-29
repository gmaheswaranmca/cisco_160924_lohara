import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headings = soup.find_all('h3')


cabs_info = []
for heading in headings:
    cab_title = heading.find('a')['title']
    cabs_info.append(cab_title)

with open('cabs_info.txt', 'w', encoding='UTF-8') as cab_file:
    for cab in cabs_info:
        cab_file.write(cab + '\n')


print('Cabs information gathered and saved to books_info.txt')