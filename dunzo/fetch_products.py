from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import csv
import time
import datetime
import handle_insert

"""This Script fetches all products for the Dunzo Website for at least a 100 stores an places it into price
The sites were pre-selected with the get_websites.py script and saved into a csv(this operation need to be repeadted)

"""

# The database should be created

CREATED_DATE = datetime.datetime.utcnow()
cities = [
    'Mumbai',
    'Bangalore',
    'Delhi',
    'Chennai',
    'Hyderabad',
    'Pune',
]

with open('sites.csv', 'r') as file:
    csv_reader = csv.reader(file)
    # Pass reader object to list() to get a list of lists
    stores = list(csv_reader)

stores_list = [item for item in stores if len(item) > 0]

driver = webdriver.Edge('../chrome_driver/msedgedriver.exe')

values = []

site = 'https://www.dunzo.com'
def fetch_product_data():
    for store in stores_list:
        driver.get(store[0])
        time.sleep(2)
        links = driver.find_element_by_css_selector(
            '.sc-10mkyz7-0.dWkYtl.tab-content').find_elements_by_css_selector(
            'a.jxbqi7-0.eTesqN')
        for link in links:
            product_link = link.get_attribute('href')
            if (stores_list.index(store) > -1):
                img_url = link.find_element_by_css_selector('img').get_attribute('src')
                values.append(
                    (
                        store[0],
                        product_link,
                        img_url,
                        CREATED_DATE,
                        CREATED_DATE,
                        CREATED_DATE,
                    )

                )
                print(values)

    handle_insert.insert_sites(values)


fetch_product_data()
