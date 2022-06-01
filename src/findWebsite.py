import cloudscraper
from bs4 import BeautifulSoup


def findWebsite(search):
    website = None
    for i in range(10):
        if website is None:
            URL = f"https://www.google.com/search?q={search}"
            scraper = cloudscraper.create_scraper()
            s = scraper.get(URL)
            soup = BeautifulSoup(s.content, 'html.parser')
            buttons = soup.findAll('div', attrs={'class': 'QqG1Sd'})
            for b in buttons:
                if b.text == "Website":
                    print(f"Found on iteration: {i}!!")
                    print(b.a['href'])
                    website = b.a['href']

    return website
