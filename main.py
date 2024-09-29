from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.edge.service import Service as service  
from utils.login import LogIn

import os


if __name__ == '__main__':
    load_dotenv()
    service = service(executable_path = os.getenv('WEBDRIVERPATH'))
    driver = webdriver.Edge(service=service)

    driver.get('https://www.instagram.com')
    LogIn(driver, os.getenv('ACCOUNTPASS'), os.getenv('ACCOUNTNAME'))
    while True: pass
    driver.close()


