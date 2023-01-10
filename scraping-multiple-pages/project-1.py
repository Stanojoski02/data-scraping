from bs4 import BeautifulSoup
import re
import pandas as pd
import requests

url = 'https://www.airbnb.ca/s/Hawaii/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=16&date_picker_type=flexible_dates&checkin=2023-01-16&checkout=2023-01-17&source=structured_search_input_header&search_type=filter_change&flexible_trip_dates%5B%5D=february'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({"Link": [''], "Title": [''], "Price": [''], "Rating": [''], 'Description': ['']})

go_on = True
PAGE = 0
while go_on:
    print(PAGE)
    PAGE += 1
    try:
        divs = soup.find('div', {'class': 'gh7uyir giajdwt g14v8520 dir dir-ltr'}).find_all('div', recursive=False)
        links = ['https://www.airbnb.ca' + i.find('a', {'class': 'bn2bl2p dir dir-ltr'}).get('href') for i in divs]
        title = [i.find('div', {'id': re.compile("title_")}).text for i in divs]
        prices = [i.find('span', {'class': 'a8jt5op dir dir-ltr'}).text[:4] for i in divs]
        ratings = [i.find('span', {'class': 't5eq1io r4a59j5 dir dir-ltr'}).get('aria-label')[:4] for i in divs if i.find('span', {'class': 't5eq1io r4a59j5 dir dir-ltr'})]
        description = [i.find('span', {'class': 't6mzqp7 dir dir-ltr'}).text for i in divs if i.find('span', {'class': 't6mzqp7 dir dir-ltr'})]
        for i in range(len(divs)):
            df = df.append({"Link": links[i], "Title": title[i], "Price": prices[i], "Rating": ratings[i], 'Description': description[i]}, ignore_index=True)
    except:
        pass
    try:
        next_page_url = 'https://www.airbnb.ca' + soup.find('a', {'aria-label': 'Next'}).get('href')
        page = requests.get(next_page_url)
        soup = BeautifulSoup(page.text, 'lxml')
    except:
        go_on = False

df.to_csv("tabee.csv")
