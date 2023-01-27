from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

PATH = 'C:\\Users\Pc4all\\Downloads\\chromedriver_win32 (3)\\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://www.instagram.com/')

time.sleep(4)

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys('')
password.send_keys('')
password.send_keys(Keys.ENTER)

time.sleep(3)
driver.get("https://www.instagram.com/stanojoski_/?next=%2F")
time.sleep(5)

followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a')
followers.click()
time.sleep(3)
go_on = True
el = []
t = 0
while go_on:
    try:
        if t == 1:
            go_on = False
        else:
            t = 1
        time.sleep(3)
        command = """
        _aano = document.querySelector("._aano");
        _aano.scrollTo(0, _aano.scrollHeight);
        var height = _aano.scrollHeight;
        return height;
        """
        driver.execute_script(command)
        time.sleep(5)
        bojan = 0
        elements = driver.find_elements(By.CSS_SELECTOR, "._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm")
        for element in elements:
            if element.text not in el:
                el.append(element.text)
                t = 0

    except:
        pass

for i in el:
    print(i)
print(len(el))

time.sleep(500)
driver.close()
