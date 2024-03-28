from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import random
import urllib.request
from bs4 import BeautifulSoup
import requests


def run_scraper():
    url = "https://idq.ro/wp-content/uploads/woo-feed/google/xml/googlefeed.xml"
    response = requests.get(url)
    html_content = response.content

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all strings that match the pattern
    all_product_links = soup.find_all(string=lambda text: text.startswith("https://idq.ro/") and text.endswith("/"))


    FILE_PATH = 'products.txt'

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    sleep(5)
    index = 0
    while(True):
        product_link = all_product_links[random.randint(0, len(all_product_links) - 1)]

        with open(FILE_PATH, 'r') as file:
            content = file.read()
            # Alternatively, use readlines() to read the file line by line
            # lines = file.readlines()
        if not product_link in content:
            print(product_link)

            with open(FILE_PATH, 'a') as file:
                file.write(product_link + "\n")

            driver.get(product_link)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"wd-carousel-container wd-gallery-images\"]")))
            image_url = driver.find_element(By.CSS_SELECTOR, "div[class=\"wd-carousel-container wd-gallery-images\"]").find_element(By.TAG_NAME, "img").get_attribute('src')
            urllib.request.urlretrieve(image_url, "image.jpg")
            title = driver.find_element(By.CSS_SELECTOR, "h1[class=\"product_title entry-title wd-entities-title\"]").text
            print(f"Title: {title}")
            description = driver.find_element(By.CSS_SELECTOR, "div[id=\"tab-description\"]").text
            print(f"Description: {description}")
            sku = driver.find_element(By.CSS_SELECTOR, "span[class=\"sku\"]").text
            print(f"SKU: {sku}")
            price = driver.find_element(By.CSS_SELECTOR, "div[class=\"row product-image-summary-wrap\"]").find_element(By.CSS_SELECTOR, "p[class=\"price\"]").text
            print(f"Price: {price}")
            driver.quit()
            return product_link, title, description, sku, price
        index += 1
        if index > len(all_product_links):
            driver.quit()
            return "no product", "no title", "no description"
        
# print(run_scraper())