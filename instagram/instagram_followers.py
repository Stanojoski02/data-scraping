from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

time.sleep(7)
driver.get("https://www.instagram.com/stanojoski_/?next=%2F")
time.sleep(5)

followers = driver.find_element(
    By.XPATH,
    '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a'
)
followers.click()

time.sleep(1)
go_on = True
el = []

t = 0
m = 0
command = """
        _aano = document.querySelector("._aano");
        _aano.scrollTo(0, _aano.scrollHeight);
        var height = _aano.scrollHeight;
        return height;
        """
time.sleep(5)
driver.execute_script(command)
while go_on:
    try:
        time.sleep(2)
        son = driver.execute_script(command)
        time.sleep(2)
        sayfaSonu = driver.execute_script(command)
        if son == sayfaSonu:
            go_on = False
        elements = driver.find_elements(By.CSS_SELECTOR, "._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm")
        for element in elements:
            if element.text not in el and "Verified" not in element.text:
                el.append(element.text)
    except:
        raise Exception

with open('followers.txt', 'a') as d:
    for i in el:
        d.write(i+"\n")

with open('followers.txt', 'r') as d:
    old_data = d.readlines()
    print([i.replace('\n', '') for i in old_data])
    print([i.replace('\n', '') for i in el])
    for j in [i.replace('\n', '') for i in old_data]:
        if j not in [i.replace('\n', '') for i in el]:
            print(ј + " unfollowed you from Instagram")

with open("followers.txt", 'w') as d:
    for i in el:
        d.write(i + '\n')

time.sleep(500)
driver.close()
