from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import csv

# Request data from the first five pages and get 100 websites for each city
#estimated number of websites


cities = [
    'Mumbai',
    'Bangalore',
    'Delhi',
    'Chennai',
    'Hyderabad',
    'Pune',
]

driver = webdriver.Edge('../chrome_driver/msedgedriver.exe')

for n in range(1, 6):
    for i in cities:
        driver.get(f'https://www.dunzo.com/{i.lower()}/fruit-and-vegetable-stores?page={n}')
        time.sleep(2)
        elements = driver.find_elements_by_css_selector('.sc-10mkyz7-0.sc-1cf264g-3.ckHxAC')
        for i in elements:
            store_link = i.find_element_by_css_selector('a').get_attribute('href')
            with open('sites.csv', 'a') as file:
                write = csv.writer(file)
                write.writerow([str(store_link), 'store'])
                print(store_link)
