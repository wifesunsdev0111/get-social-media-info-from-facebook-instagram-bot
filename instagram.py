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
    
    # USERNAME = "12143066090"
    # PASSWORD = "Vre32#2$5%12"

    # chrome_options = Options()
    # prefs = {"profile.default_content_setting_values.notifications" : 2}
    # chrome_options.add_experimental_option("prefs",prefs)

    # driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()
    # driver.get("https://instagram.com")
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"_a9-- _ap36 _a9_0\"]")))
    # accept_cookie_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"_a9-- _ap36 _a9_0\"]")
    # accept_cookie_button.click()
    # sleep(5)
    # input_username = driver.find_element(By.CSS_SELECTOR, "input[name=\"username\"]")
    # input_username.send_keys(USERNAME)

    # input_password = driver.find_element(By.CSS_SELECTOR, "input[name=\"password\"]")
    # input_password.send_keys(PASSWORD)

    # login_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    # login_button.click()
    # sleep(5)

    # try:
    #     not_now_button = driver.find_element(By.CSS_SELECTOR, "div[class=\"x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37\"]")
    #     not_now_button.click()
    # except:
    #     pass

    firefox_profile_directory = 'C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/lbfn82ix.default-release'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)


    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get("https://instagram.com/")

    search_button_parent= driver.find_element(By.CSS_SELECTOR, "div[class=\"x1iyjqo2 xh8yej3\"]")
    search_button = search_button_parent.find_elements(By.XPATH, "./*")[1]
    search_button.click()

    search_input = driver.find_element(By.CSS_SELECTOR, "input[class=\"x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j\"]")
    search_input.send_keys("coca cola ")
    sleep(2)

    search_result_parent = driver.find_element(By.CSS_SELECTOR, "div[class=\"x9f619 x78zum5 xdt5ytf x1iyjqo2 x6ikm8r x1odjw0f xh8yej3 xocp1fn\"]")
    search_result_a = search_result_parent.find_elements(By.TAG_NAME, "a")[0]
    search_result_url = search_result_a.get_attribute("href")
    driver.get(search_result_url)

    sleep(3)



    # Get the initial page height
    initial_height = 0
    count = 0
    try:
        # scroll_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"x193iq5w x1xwk8fm\"]")))

        while True:
            # Scroll to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            posts = driver.find_elements(By.CSS_SELECTOR, "div[class=\"x1lliihq x1n2onr6 xh8yej3 x4gyw5p x2pgyrj xbkimgs xfllauq xh8taat xo2y696\"]")
            sleep(2)
            try:
                scroll_height = driver.execute_script("return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")
                # end_contet = driver.find_element(By.CSS_SELECTOR, "div[class=\"x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np x1a02dak xqjyukv x1qjc9v5 x1oa3qoh xl56j7k\"]")
                # if end_contet:
                #     print(f"Scroll End", end_contet.text)
                #     break
                if len(posts) > 20:
                    break
                print(initial_height, scroll_height)
                if initial_height == scroll_height and scroll_height != 0:
                    break
                else:
                    initial_height = scroll_height
            except:
                continue
    except:
        posts = driver.find_elements(By.CSS_SELECTOR, "div[class=\"x1lliihq x1n2onr6 xh8yej3 x4gyw5p x2pgyrj xbkimgs xfllauq xh8taat xo2y696\"]")
        pass
    print(f'post length = ', len(posts))
    sleep(3)

    results = []
    for index, post in enumerate(posts):
        print(len(posts), index)
        try:
            driver.execute_script("arguments[0].scrollIntoView(false); window.scrollBy(0, 0);", post)
            url_a = post.find_element(By.TAG_NAME, "a")
            driver.execute_script("arguments[0].click();", url_a)
        except:
            pass
        
        sleep(3)
        
        try:
            post_parent_div = driver.find_element(By.CSS_SELECTOR, "ul[class=\"_a9z6 _a9za\"]")
            post_div = post_parent_div.find_elements(By.TAG_NAME, "div")[0]
            post_data = post_div.text
            post_data_com = post_data.replace("\n", " ")
            print(f'post data = ',  index, post_data_com)
            results.append(post_data_com)
        except:
            pass

        try:
            close_dev = driver.find_element(By.CSS_SELECTOR, "div[class=\"x160vmok x10l6tqk x1eu8d0j x1vjfegm\"]")
            driver.execute_script("arguments[0].click();", close_dev)
            driver.execute_script("arguments[0].click()", close_dev)
        except:
            pass

    print(results)

    driver.quit()    
    return results