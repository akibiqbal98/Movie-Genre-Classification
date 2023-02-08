# 1. Movie name,
# 2. Year,
# 3. description,
# 5. rating,
# 6. Gerne.

# -------------------------><-----------------
import re
import sys
import json 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# def create_driver_and_wait(waiting_time=10):
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Create an instance of Chrome
driver = webdriver.Chrome(options=chrome_options)

# wait for the page to load
driver.implicitly_wait(50)
wait = WebDriverWait(driver, 50)

# Create an instance of Chrome
# return driver, wait

driver.get('https://www.imdb.com/search/title/?title_type=feature&release_date=2000-01-01,2023-12-31&user_rating=5.0,&languages=en&count=250')

data = []


def create_driver_and_wait(waiting_time=10):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Create an instance of Chrome
    driver = webdriver.Chrome(options=chrome_options)

    # wait for the page to load
    driver.implicitly_wait(waiting_time)
    wait = WebDriverWait(driver, waiting_time)

    # Create an instance of Chrome
    return driver, wait


def get_innerHTML(element: WebElement):
    # name = element.find_element(By.CSS_SELECTOR, "div#main h3 a").text
    year = element.find_element(By.CSS_SELECTOR, "div#main h3 span.lister-item-year").text
    # rating = element.find_element(By.CSS_SELECTOR, "div#main div.ratings-bar strong").text
    
    genre, description = element.find_elements(By.CSS_SELECTOR, 'div#main p.text-muted')
    
    # reg_year = re.search(r"\d{4}", year)
    # print(reg_year.group())
    
    return {
        "Name": element.find_element(By.CSS_SELECTOR, "div#main h3 a").text,
        "Year": re.search(r"\d{4}", year).group(0),
        "Rating": element.find_element(By.CSS_SELECTOR, "div#main div.ratings-bar strong").text,
        "Description": description.text , 
        "Genre": genre.find_element(By.CSS_SELECTOR,"span.genre").text.split(",")
        
    }


def change_page(by, value):
    element: WebElement = wait.until(EC.presence_of_element_located((by, value)))
    driver.execute_script("arguments[0].click();", element)
    sleep(20)

# def change_page():
#     # next page button
#     XPATH = "//div[@id='main']/div[@class='desc']/a[@class='lister-page-next']"
#     element: WebElement = wait.until(EC.presence_of_element_located((By.XPATH, XPATH)))
#     # print(element_.get_attribute("outerHTML"))
#     # element.click()  # Not working
#     driver.execute_script("arguments[0].click();", element) 


# Navigate to a website
url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2000-01-01,2023-12-31&user_rating=5.0,&languages=en&count=250'
driver.get(url)

# elements: WebElement = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#main div.lister-item')))
# data = list(map(get_innerHTML, elements[:20]))
# print(data)


all_elements = []

page_no = 174

for indx in range(page_no):
    while(True):
        try:
            elements: WebElement = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#main div.lister-item')))
            all_elements.extend(list(map(get_innerHTML, elements[:])))
            
        except Exception as e:
            print(e)
            continue
        
        else:
            print(len(all_elements))
            if indx != page_no - 1:
                change_page(By.CSS_SELECTOR,  'div#main div.desc a.lister-page-next')
                sleep(10) 
            break

print(all_elements)

# def format_scrappy_data(data: list[tuple]):
#     return [
#         {
#             "Movie Name": a,
#             "Release Year": b,
#             "Rating": c,
#             "Description": d,
#             "Genre": e,
#         } for a, b, c, d, e in data
#     ]


# # print formatted data using json to a file

# with open('movie_data.json', 'w') as f:
#     json.dump(format_scrappy_data(all_elements), f, indent=2)


# pause for 10 seconds
sleep(50)
