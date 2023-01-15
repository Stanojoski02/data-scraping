from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

PATH = 'C:\\Users\Pc4all\\Downloads\\chromedriver_win32 (3)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://twitter.com/i/flow/login')
time.sleep(4)

email = ''
pw = ''
un = ''
celeb = ''

# login
username = driver.find_element(By.CSS_SELECTOR, 'input[name="text"]')
username.send_keys(email)
username.send_keys(Keys.ENTER)
time.sleep(2)

try:
    username = driver.find_element(By.CSS_SELECTOR, 'input[name="text"]')
    username.send_keys(un)
    username.send_keys(Keys.ENTER)
except:
    pass
time.sleep(2)
password = driver.find_element(By.NAME, 'password')
password.send_keys(pw)
password.send_keys(Keys.ENTER)
time.sleep(2)
# Search
search = driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Search Twitter']")
search.send_keys(celeb)
search.send_keys(Keys.ENTER)
time.sleep(2)
people = driver.find_element(By.LINK_TEXT, 'People')
people.click()
time.sleep(1)
celeb = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]')
celeb.click()
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all(
    'div', {'class': 'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0'}
)

tweets = []
while True:
    for post in postings:
        if post.text not in tweets:
            tweets.append(post.text+'\n')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all(
        'div', {'class': 'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0'}
    )
    if len(tweets) >10:
        break
for i in tweets:
    print(i)

time.sleep(150)
