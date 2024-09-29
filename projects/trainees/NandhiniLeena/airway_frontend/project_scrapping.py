import requests
from bs4 import BeautifulSoup
url="https://flykingfisher.com/"
airplane_res=requests.get(url)
soup=BeautifulSoup(airplane_res.content,'html.parser')
headings=soup.find_all('h2')
with open('airplane_headingd.txt','w',encoding='utf-8') as airplane_file:
    for heading in headings:
        airplane_file.write(heading.text+"\n")

print("airplane gathered")