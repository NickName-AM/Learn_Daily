# Scraping Test on https://thehackernews.com/

import requests
from bs4 import BeautifulSoup

req = requests.get("https://thehackernews.com/")

soup = BeautifulSoup(req.content, 'html.parser')

# The required data. But, contains everything (tags, links, headlines, etc.)
raw_news = soup.find_all('a', class_ = 'story-link')

with open('news.txt', 'w') as f:
    for news in raw_news:

        # Get the link for one part
        b_link = news.get('href')

        # Get the headline for one part
        headline = news.find('h2', class_ = 'home-title').text
        
        # Write it into the file
        f.write(headline + '\nSource: ' + b_link + '\n' + '\n\n')