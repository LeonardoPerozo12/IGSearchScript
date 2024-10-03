from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.edge.service import Service
from utils.login import LogIn
from utils.scroll import Scroll
from utils.scroll import InspectAccount
import os

if __name__ == '__main__':
    load_dotenv()  # Load environment variables from .env file

    # Set up the Edge WebDriver service with the path specified in .env
    service = Service(executable_path=os.getenv('WEBDRIVERPATH'))
    driver = webdriver.Edge(service=service)

    # Open Instagram login page
    driver.get('https://www.instagram.com')

    # Log in using the account credentials from .env
    LogIn(driver, os.getenv('ACCOUNTPASS'), os.getenv('ACCOUNTNAME'))

    # Scroll through the feed and open profiles in new tabs
    Scroll(driver)

    InspectAccount(driver, account_url)
    # try out thew new InspectAccount Function
    # before trying anything with Instagram's API
    

    # Keep the browser open
    while True: pass

    # Close the browser when done
    driver.close()
    # try using the function driver.quit() to close all of the tabs in the program, instead of closing the tab it is in
