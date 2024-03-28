from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import secrets

def run(search_index):
    
    EMAIL_ADDRESS = "leonmarsh0111@outlook.com"
    PASSWORD = "@adB540Ec$12"
    
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://facebook.com")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title=\"Allow all cookies\"]")))
    accept_cookie_button = driver.find_element(By.CSS_SELECTOR, "button[title=\"Allow all cookies\"]")
    accept_cookie_button.click()

    input_email = driver.find_element(By.CSS_SELECTOR, "input[id=\"email\"]")
    input_email.send_keys(EMAIL_ADDRESS)

    input_password = driver.find_element(By.CSS_SELECTOR, "input[id=\"pass\"]")
    input_password.send_keys(PASSWORD)

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    login_button.click()
    sleep(5)

        
    driver.get("https://www.facebook.com/search/top?q=" + search_index)

    sleep(3)

    try:
        # scroll_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"x193iq5w x1xwk8fm\"]")))

        while True:
            # Scroll to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            posts = driver.find_elements(By.CSS_SELECTOR, "div[class=\"x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z\"]")
            sleep(2)
            try:
                end_contet = driver.find_element(By.CSS_SELECTOR, "div[class=\"x1n2onr6 x1ja2u2z x9f619 x78zum5 xdt5ytf x2lah0s x193iq5w xz9dl7a\"]")
                if end_contet:
                    print(f"Scroll End", end_contet.text)
                    break
            except:
                continue
    except:
        posts = driver.find_elements(By.CSS_SELECTOR, "div[class=\"x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z\"]")
        pass
    
    sleep(3)
    
    results = []
    for index, post in enumerate(posts):
        result = {}
        print(len(posts), index)
        try:
            driver.execute_script("arguments[0].scrollIntoView(false); window.scrollBy(0, 0);", post)
        except:
            pass
        sleep(2)
        try:
            post_data_span = post.find_element(By.CSS_SELECTOR, "span[class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h\"]")
            
            try:
                see_more_button = post_data_span.find_element(By.XPATH, ".//div[contains(text(), 'See more')]")
                driver.execute_script("arguments[0].click();", see_more_button)
            except:
                pass
            
            post_data = post_data_span.text
            
           

            post_title_h3 = post.find_element(By.CSS_SELECTOR, "h3[class=\"x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz x1gslohp x1yc453h\"]")
            post_title = post_title_h3.text
            
            
            post_date_span_parent =  post.find_element(By.CSS_SELECTOR, "span[class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa xo1l8bm xi81zsa x1yc453h\"]")
            post_date_span = post_date_span_parent.find_elements(By.CSS_SELECTOR, "span[class=\"x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j\"]")[0]
            get_post_date = post_date_span.text
        
            try:
                current_year = datetime.now().year
                post_date_string = str(current_year) + " " + get_post_date
                post_date_format = "%Y %B %d at %I:%M %p"
                post_date = datetime.strptime(post_date_string, post_date_format)
                
                current_date = datetime.now()
                
                time_difference = current_date - post_date
                different_day = time_difference.days
            except:
                different_day = 2
            
            if different_day <= 14:
                post_id = secrets.token_hex(8)
                result['id'] = str(post_id)
                result['post_title'] = post_title.replace("\n", "")
                result['post_data'] = post_data.replace("\n", "")
                result['post_date'] = get_post_date
                # print(f'result = ', result)                
                results.append(result)
            else:
                continue
            
            
        except:
            continue
        
    
    driver.quit()    
    return results