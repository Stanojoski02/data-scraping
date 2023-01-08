from bs4 import BeautifulSoup
import pandas as pd
import re
import requests

url = 'https://www.worldometers.info/world-population/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")

html_table = soup.find('table', {'class':'table table-striped table-bordered table-hover table-condensed table-list'})
html_table = html_table.find_all(['tr', 'th'])

years = [html_table[0].find('th').text]
population = [html_table[0].find_all("th")[1].text]
year_percentage_change = [html_table[0].find_all("th")[2].text]
year_change = [html_table[0].find_all('th')[3].text]
median_age = [html_table[0].find_all('th')[4].text]
fertility_rate = [html_table[0].find_all('th')[5].text]
density_p_km = [html_table[0].find_all('th')[6].text]

for i in html_table:
    if i.find('td'):
        years.append(i.find('td').text)
        population.append(i.find_all('td')[1].text)
        year_percentage_change.append(i.find_all('td')[2].text)
        year_change.append(i.find_all('td')[3].text)
        median_age.append(i.find_all('td')[4].text)
        fertility_rate.append(i.find_all('td')[5].text)
        density_p_km.append(i.find_all('td')[6].text)

table = pd.DataFrame(
    {
    years[0]: years[1:],
    population[0]: population[1:],
    year_percentage_change[0]: year_percentage_change[1:],
    year_change[0]: year_change[1:],
    median_age[0]: median_age[1:],
    fertility_rate[0]: fertility_rate[1:],
    density_p_km[0]: density_p_km[1:]
    }
)
print(table)
