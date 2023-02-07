# 1. Movie name,
# 2. Year,
# 3. description,
# 5. rating,
# 6. Gerne.

# -------------------------><-----------------
import re
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# def create_driver_and_wait(waiting_time=10):


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Create an instance of Chrome
driver = webdriver.Chrome(options=chrome_options)

# wait for the page to load
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# Create an instance of Chrome
# return driver, wait

driver.get('https://www.imdb.com/search/title/?title_type=feature&release_date=2000-01-01,2023-12-31&user_rating=5.0,&languages=en&count=250')

data = []


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
        "Description": description.text,
        "Genre": genre.find_element(By.CSS_SELECTOR, "span.genre").text.split(",")
    }


def change_page(by, value):

    # find the next button element
    next_button = driver.find_element_by_css_selector('div#main div#desc a.lister-page-next')

    # click on the next button to go to the next page
    next_button.click()

    # wait for the page to load
    time.sleep(2)


elements: WebElement = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#main div.lister-item')))

data = map(get_innerHTML, [elements[:10]])

print(data)


# tried to make list generator

# data = (d for d in data, d for d in map(get_innerHTML, [*elements[10:20]]))
# data = (*data, *map(get_innerHTML, [*elements[20:30]]))

# # for d in data:
# #     print(d)
# print(sys.getsizeof(data), sys.getsizeof(list(data)), type(data))
