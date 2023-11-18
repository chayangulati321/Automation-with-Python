from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import time
from datetime import datetime as dt

service = Service('C://Users//HP//Desktop//Material//UpSkill//Automation//chromedriver-win64//chromedriver-win64//chromedriver.exe')

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')  # to disable nav-bar
    options.add_argument('start-maximized')   # to maximize sc`reen size
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(service=service, options=options)
    driver.get('http://automated.pythonanywhere.com/login/')
    return driver

def clean_text(text):
    temp_value = float(text.split(": ")[1])
    save_file(temp_value)

def save_file(temp):
    filename = dt.now().strftime("%Y-%m%d.%H%M%S")
    with open(f'{filename}.txt', 'w') as file:
        file.write(str(temp))

def main():
    driver = get_driver()
    driver.find_element(by='id', value='id_username').send_keys('automated')
    time.sleep(1)
    driver.find_element(by='id', value='id_password').send_keys('automatedautomated' + Keys.RETURN)
    time.sleep(1)
    driver.find_element(by='xpath', value='/html/body/nav/div/a').click()

    for i in range(10):
        time.sleep(2)
        text = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]').text
        clean_text(text)


main()

