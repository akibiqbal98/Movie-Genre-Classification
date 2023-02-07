import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Feature Film, Released between 2000-01-01 and 2023-12-31, 
# User Rating at least 5, English Language
# link = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2000-01-01,2023-12-31&user_rating=5.0,&languages=en&count=250'

driver = webdriver.Chrome()
# wait for 10 seconds for the page to load
driver.implicitly_wait(50)

driver.get('https://www.imdb.com/search/title/?title_type=feature&release_date=2000-01-01,2023-12-31&user_rating=5.0,&languages=en&count=250')

links = driver.find_elements("xpath", '//div[@class="lister-item mode-advanced"]')

for link in links:
    print(link.get_attribute("innerHTML"))
    name = driver.find_element("xpath", "//")
    break


names = []
years = []
genres = []
descriptions = []

# # loop through each result and scrape data
# for result in results:
#     name = result.find_element_by_xpath('.//a').text
#     year = result.find_element_by_xpath('.//span[@class="lister-item-year text-muted unbold"]').text
#     genre = result.find_element_by_xpath('.//span[@class="genre"]').text
#     description = result.find_element_by_xpath('.//p[@class="text-muted"]').text
    
#     # append data to lists
#     names.append(name)
#     years.append(year)
#     genres.append(genre)
#     descriptions.append(description)
# time.sleep(5)
# # create pandas dataframe
# df = pd.DataFrame({'Name': names, 'Year': years, 'Genre': genres, 'Description': descriptions})

# # save to csv file
# df.to_csv('imdb_data.csv', index=False)

# # # close chromedriver
# # # driver.quit()