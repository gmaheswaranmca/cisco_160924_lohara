import requests
from bs4 import BeautifulSoup

def scrape_books(limit=50):
    """Scrape books data from a website."""
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = []
    for idx, book in enumerate(soup.find_all('article', class_='product_pod')[:limit], start=1):  
        title = book.find('h3').text
        price = book.find('p', class_='price_color').text
       
        stock = 10  
        books.append((str(idx), title, price, stock))  

    print(f"Scraped books: {books}") 
    return books




