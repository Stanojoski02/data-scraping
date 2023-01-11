import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.carpages.ca/used-cars/search/?category_id=2'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'Title': [''], 'Color': [''], 'Price': [''], 'Links': ['']})
go_on = True
PAGE = 0

while go_on:
    if PAGE <= 5:
        print(PAGE)
        PAGE += 1
        ads = soup.find_all('div', {'class': 'media soft push-none rule'})
        links = [
            'https://www.carpages.ca/' + i.find('a', {'class': 'media__img media__img--thumb'}).get('href').strip() 
            for i in ads
        ]
        titles = [i.find('h4', {'class': 'hN'}).text.strip() for i in ads]
        prices = [i.find('strong', {'class': 'delta'}).text.strip() for i in ads]
        colors = [ 
            i.find_all('div', {'class': 'grey l-column l-column--small-6 l-column--medium-4'})[1].text.strip()
            for i in ads
        ]
        
        for i in range(len(ads)):
            df = df.append(
                {'Title': titles[i], 'Color': colors[i], 'Price': prices[i], 'Links': links[i]},
                ignore_index=True
            )
        next_page_url = 'https://www.carpages.ca/' + soup.find('a', {'class': 'nextprev'}).get('href')
        page = requests.get(next_page_url)
        soup = BeautifulSoup(page.text, 'lxml')
    else:
        go_on = False

df.to_csv("N.csv")
