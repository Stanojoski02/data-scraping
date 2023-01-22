from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import re
import pandas as pd

PATH = "C:\\Users\Pc4all\\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://www.indeed.com/jobs?q=&l=United%20States&from=searchOnHP')
search_for_job = driver.find_element(By.ID, 'text-input-what')
search_for_job.send_keys('Python Junior Developer')
search_button = driver.find_element(By.CLASS_NAME, 'yosegi-InlineWhatWhere-primaryButton')
search_button.click()

soup = BeautifulSoup(driver.page_source, 'lxml')
divs = soup.find_all('div', {'class': 'job_seen_beacon'})
go_on = 0
df = pd.DataFrame({'Title': [''], 'Salary': [''], 'Link': ['']})

while go_on<2:
    print(go_on)
    time.sleep(2)
    go_on +=1
    titles = []
    salarys = []
    urls = []
    for i in divs:
        if i.find("a", {'class':'jcs-JobTitle'}):
            titles.append(i.find("a", {'class':'jcs-JobTitle'}).text)
        else:
            titles.append(" ")
        if i.find(string=re.compile("\$")):
            salarys.append(i.find(string=re.compile("\$")))
        else:
            salarys.append(" ")
        if i.find('a', {'class': re.compile('jcs-JobTitle')}).get('href'):
            urls.append('https://www.indeed.com' + i.find('a', {'class': re.compile('jcs-JobTitle')}).get('href'))
        else:
            urls.append(" ")

    for i in range(len(titles)):
        try:
            df = df.append(
                {'Title': str(titles[i]).replace("]", '').replace('[', ''), 'Salary': str(salarys[i]).replace("]", '').replace('[', ''), 'Link': str(urls[i]).replace("]", '').replace('[', '')},
                ignore_index=True
            )
        except:
            pass
    salery = soup.find_all('div', {'class': 'attribute_snippet'})
    next_page_url = soup.find('a', {"data-testid": 'pagination-page-next', "aria-label": 'Next Page'})
    try:
        new_page = requests.get(next_page_url)
        soup = BeautifulSoup(new_page.text, 'lxml')
    except:
        pass

      
df.drop(index=df.index[0], axis=0, inplace=True)
df.to_csv("my_csv.csv")
