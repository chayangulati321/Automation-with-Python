from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time

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
    driver.get('http://automated.pythonanywhere.com')
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]')
    time.sleep(2)
    return element.text


print(main())

