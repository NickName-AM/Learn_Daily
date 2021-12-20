import sys
import requests
from bs4 import BeautifulSoup

def usage():
    print(f"Usage: py {sys.argv[0]} 'SEARCH_TEXT'\n")
    exit()

if len(sys.argv) < 2:
    usage()

data = sys.argv[1]
# while len(data) < 1 or len(data) > 20:
#     data = str(input("Search: "))

req = requests.get(f"https://myanimelist.net/search/all?q={data}&cat=all")

soup = BeautifulSoup(req.content, 'html.parser')


# For Anime Info

rows = soup.find_all('div', class_ = "information di-tc va-t pt4 pl8")

# rows is a 'list' of relevant data from anime tab
FILENAME = 'MyAnimeListSearch.txt'

with open(FILENAME, 'w') as f:

    for row in rows:
        # The heading/title of the row
        title = row.find('a', class_ = "hoverinfo_trigger fw-b fl-l").string

        # The link to the webpage
        link = row.find('a', class_ = "hoverinfo_trigger fw-b fl-l").get('href')

        # Episodes, ratings, etc.
        info = row.find('div', class_ = 'pt8 fs10 lh14 fn-grey4').text.strip()
        
        f.write("\nTitle: " + title + '\nSauce: ' + link + '\n' + info + '\n\n')

print(f"[+] Data written in '{FILENAME}'")
