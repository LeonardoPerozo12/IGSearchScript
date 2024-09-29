from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCon


def LogIn(driver: webdriver.Edge, password: str, Username: str):

    usernameField = WebDriverWait(driver, 10).until(
        ExpCon.visibility_of_element_located((By.XPATH, "//input[@aria-label='Phone number, username, or email']"))
    )
    usernameField.send_keys(Username)

    passwordField = WebDriverWait(driver, 10).until(
        ExpCon.visibility_of_element_located((By.XPATH, "//input[@aria-label='Password']"))
    )  
    passwordField.send_keys(password) 

    loginBtn = WebDriverWait(driver, 10).until(
        ExpCon.visibility_of_element_located((By.XPATH, "//button//div[text() = 'Log in']"))
    )
    loginBtn.click()
    
    notNowBtn = WebDriverWait(driver, 10).until(
        ExpCon.visibility_of_element_located((By.XPATH, "//div[text() = 'Not now']"))
    )
    notNowBtn.click()

    notNowBtn2 = WebDriverWait(driver, 10).until(
        ExpCon.visibility_of_element_located((By.XPATH, "//button[text() = 'Not Now']"))
    )
    notNowBtn2.click()