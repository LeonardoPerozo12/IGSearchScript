from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExpCon



def Scroll(driver: webdriver.Edge):
    posts = driver.find_elements(By.TAG_NAME, 'article')

    for i, post in enumerate(posts):

        postHeader = post.find_element(By.TAG_NAME, 'div')
        postSections = postHeader.find_elements(By.TAG_NAME, 'div')

        for j, post2 in enumerate(postSections):
            if j == 0:
                postAnchor = post2.find_element(By.TAG_NAME, 'a')
                postUrl = postAnchor.get_attribute('href')

        postUrl.
                 

