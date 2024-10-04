from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCon
import time

def Scroll(driver: webdriver.Edge):
    # Wait for posts to load
    time.sleep(5)
    
    # Find the posts (typically they are inside <article> tags on Instagram)
    posts = driver.find_elements(By.TAG_NAME, 'article')

    for i, post in enumerate(posts):
        try:
            # Extract post header and sections (this part depends on Instagram's DOM structure)
            postHeader = post.find_element(By.TAG_NAME, 'div')
            postSections = postHeader.find_elements(By.TAG_NAME, 'div')

            for j, post2 in enumerate(postSections):
                if j == 0:
                    # Fetch the anchor tag which contains the post's URL
                    profileAnchor = post2.find_element(By.TAG_NAME, 'a')
                    profileUrl = profileAnchor.get_attribute('href')
                    print(f"Profile {i + 1} URL: {profileUrl}")

                    InspectAccount(driver, profileUrl)

                    # Open the profile URL in a new tab
                    # driver.execute_script(f"window.open('{profileUrl}', '_blank');")

                    # # Switch to the new tab (most recent tab)
                    # driver.switch_to.window(driver.window_handles[-1])

                    # # Here you can interact with the profile, if needed

                    # # Switch back to the original tab (first tab)
                    # driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print(f"Error processing post {i + 1}: {e}")
    
    # Scroll down the page to load more posts if needed
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Wait for new posts to load



def InspectAccount(driver: webdriver.Edge, account_url: str) -> bool:
    
    # Visit the account's URL in a new tab
    driver.execute_script(f"window.open('{account_url}', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    
    # Find the header element
    header = WebDriverWait(driver, 30).until(
        ExpCon.visibility_of_element_located((By.TAG_NAME, "header"))
    )
    
    # Find all section elements within the header
    sections = header.find_elements(By.TAG_NAME, "section")
    
    for i, section in enumerate(sections, start=1):
        if i == 3:
            # The third section contains the post, follower, and following count inside a ul element
            ul = section.find_element(By.TAG_NAME, "ul")
            
            # The second li element contains the follower count
            follower_span_obj = ul.find_elements(By.TAG_NAME, "li")[1]
            
            # The a tag says "followers" and the span tag contains a span with the count
            follower_count = follower_span_obj.find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").text
            
            print(f"Follower count: {follower_count}")
    


            # # Here you can interact with the profile, if needed

            # # Switch back to the original tab (first tab)

    # Close the tab and switch back to the main tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
