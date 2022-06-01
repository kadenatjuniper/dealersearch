import cloudscraper
from bs4 import BeautifulSoup


def keywordCheck(website, keyword):
    result = None
    for i in range(10):
        if result is None:
            URL = f'https://www.google.com/search?q=site:{website} "{keyword}"'
            scraper = cloudscraper.create_scraper()
            s = scraper.get(URL)
            soup = BeautifulSoup(s.content, 'html.parser')
            resultObject = soup.find('div', attrs={'class': 'yuRUbf'})
            if resultObject:
                if resultObject.a['href']:
                    result = resultObject.a['href']
                else:
                    result = 'yes'

    return result


# print(keywordCheck('5dsolutionsinc.com/3d-grade-management-system/', "topcon"))
