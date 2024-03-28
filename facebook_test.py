from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import secrets

def run(search_index):
    
    
    firefox_profile_directory = 'C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/lbfn82ix.default-release'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get("https://www.facebook.com/search/top?q=" + search_index)
    # sleep(10)

        
    # input_field = driver.find_element(By.CSS_SELECTOR, "input[class=\"x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w xnwf7zb x40j3uw x1s7lred x15gyhx8 x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8\"]")
    # input_field.send_keys(search_index)
    # input_field.send_keys(Keys.RETURN)

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
                print(f'result = ', result)                
                results.append(result)
            else:
                continue
            
            
        except:
            continue
        
    
    driver.quit()    
    return results

