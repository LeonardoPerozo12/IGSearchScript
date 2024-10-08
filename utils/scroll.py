from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCon
import time
import re

def Scroll(driver: webdriver.Edge):
    # Wait for posts to load
    time.sleep(2.5)
    Valid_Profiles = []
    ProfileUrls = []
    
    # Find the posts (typically they are inside <article> tags on Instagram)

    while len(Valid_Profiles) < 10:
        posts = driver.find_elements(By.TAG_NAME, 'article')
        
        for i, post in enumerate(posts):
            try:
                # Extract post header and sections (this part depends on Instagram's DOM structure)
                postHeader = post.find_element(By.TAG_NAME, 'div')
                postSections = postHeader.find_elements(By.TAG_NAME, 'div')

                for j, post_2 in enumerate(postSections):
                    if j == 0:
                        # Fetch the anchor tag which contains the post's URL
                        profileAnchor = post_2.find_element(By.TAG_NAME, 'a')
                        profileUrl = profileAnchor.get_attribute('href')
                        
                        if profileUrl in ProfileUrls:
                            continue
                        
                        print(f"Profile {i + 1} URL: {profileUrl}")
                        Account_is_Valid, bio_email_value = InspectAccount(driver, profileUrl)
                        if Account_is_Valid == True:
                            Valid_Profiles.append(bio_email_value)
                            ProfileUrls.append(profileUrl)
            except Exception as e:
                print(f"Error processing post {i + 1}: {e}")
                
        # Check that there is only one window open
        while len(driver.window_handles) > 1:
            # Close the last tab
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1.5)
            driver.close()
            time.sleep(1.5)
        
        # Scroll down the page to load more posts
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Wait for new posts to load
    
    print(f"Valid Profiles : {Valid_Profiles}")
    print(f"Profile URLs : {ProfileUrls}")


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
        # The third section contains the post, follower, and following count inside a ul element
        if i == 3:
            ul = section.find_element(By.TAG_NAME, "ul")
            
            # The second li element contains the follower count
            follower_span_obj = ul.find_elements(By.TAG_NAME, "li")[1]
            
            # The a tag says "followers" and the span tag contains a span with the count
            follower_count = follower_span_obj.find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").text
            
            # Convert follower count from string to number
            if "K" in follower_count:
                follower_count = float(follower_count.replace("K", "")) * 1000
            elif "M" in follower_count:
                follower_count = float(follower_count.replace("M", "")) * 1000000
            else:
                # Remove all non-numeric characters
                follower_count = "".join(filter(str.isdigit, follower_count))
                follower_count = int(follower_count)
                
            print(f"Follower count: {follower_count}")
            
            if follower_count >= 50000:
                # Get email from the bio (fourth section)
                bio_section = sections[3]
                parent_bio_div = bio_section.find_element(By.TAG_NAME, 'div')
                bio_text = parent_bio_div.text
                
                bio_email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z-]+'
                bio_email = re.search(bio_email_regex, bio_text) 
                bio_email_value = bio_email.group() if bio_email else None
                if bio_email:
                    print(f"Email: {bio_email}")
                    account_valid = True
                else:
                    account_valid = False
            else:
                account_valid = False
                bio_email_value = None
    
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2.5)
    
    return account_valid, bio_email_value
