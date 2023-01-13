from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = 'C:\\Users\Pc4all\\Downloads\\chromedriver_win32 (3)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://google.com')

google_box = driver.find_element(By.CLASS_NAME, 'gLFyf')
google_box.send_keys('Top 100 movies of all time')
google_box.send_keys(Keys.ENTER)

time.sleep(7)

link_of_top_100 = driver.find_element(By.XPATH, '//*[@id="rso"]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3')
link_of_top_100.click()

time.sleep(1)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight/2.25)')
driver.save_screenshot('C:\\Users\\Pc4all\\Desktop\\web-scraping\\screen1.png')
poster = \
    driver.find_element(
        By.XPATH, '//*[@id="main"]/div/div[3]/div/div[25]/div[2]/a/img'
    ).screenshot('C:\\Users\\Pc4all\\Desktop\\web-scraping\\screen2.png')

time.sleep(100)
