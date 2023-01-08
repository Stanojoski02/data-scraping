import pandas as pd
from bs4 import BeautifulSoup
import requests


url = 'https://www.nfl.com/standings/league/2019/REG'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
html_table = soup.find(
    'table', {
        'class': "d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings-"
                 "-detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}"
    }
)

headers = html_table.find_all('th')
headers = [i.text for i in headers]

rows = []
for i in soup.find_all("tr"):
    row = [j.text for j in i.find_all('td')]
    if row:
        rows.append(row)

table = pd.DataFrame(rows)
table.columns = headers

print(table)
