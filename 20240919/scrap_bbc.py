#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
import json 
# URL of News Site
url = "https://www.bbc.com/news"
html_file_name = 'news_html.html'
news_file_name = 'news_json.json'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
print(response.status_code)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    with open(html_file_name,'w', encoding="utf-8") as html_db: 
        html = soup.prettify()
        #print(type(html))
        html_db.write(html)
    # Find all article headlines (BBC News uses 'h3' tags for headlines)
    headlines = soup.find_all('h2')

    # Print the headlines
    #for idx, headline in enumerate(headlines):
    #    print(f"{idx + 1}. {headline.get_text(strip=True)}")
    news = [{f'news{idx + 1}': str(headline)} for idx, headline in enumerate(headlines)]
    ####print(news)

    #json_str = json.dumps(news)    
    #with open(news_file_name,'w') as news_db: 
    #    news_db.write(json_str)
    
    with open(news_file_name,'w') as news_db:
        json.dump(news, news_db)
else:
    print(f"Failed to retrieve BBC News. Status code: {response.status_code}")
