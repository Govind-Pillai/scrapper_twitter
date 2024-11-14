#importing necessary libraries
import time
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data={}

# Set up Chrome driver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run headless
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Read the CSV file
twitterlinks = "C:/Users/Govind/Python_Study/Webapp/twitter_links.csv"  # Replace with your file path
links = pd.read_csv(twitterlinks)
for index, row in links.iterrows():
    url = row["Website"]
    time.sleep(5)
    driver = webdriver.Chrome(service=chrome_options, options=chrome_options)
    driver.get(url)
    data={"url":url}
    try:
    # Bio
        data[bio] = driver.find_element(By.XPATH, "//div[@data-testid='UserDescription']").text
    except:
        data[bio]="Not Avaialable"
    try:
    # Following Count
        data[following_count] = driver.find_element(By.XPATH, "//a[contains(@href, '/following')]/span").text
    except:
        data[following_count] = 0
    try:
    # Followers Count
        data[followers_count] = driver.find_element(By.XPATH, "//a[contains(@href, '/followers')]/span").text
    except:
        data[followers_count] = 0
    # Location (if available)
    try:
        data[location] = driver.find_element(By.XPATH, "//span[@data-testid='UserLocation']").text
    except:
        data[location] = '"Not available"'

    # Website (if available)
    try:
        data[website] = driver.find_element(By.XPATH, "//a[@data-testid='UserUrl']").get_attribute("href")
    except:
        data[website] = "N.A."

    with open("C:\Users\Govind\Python_Study\Webapp\twitterscrape.csv", mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["URL", "Bio", "Following Count", "Followers Count", "Location", "Website"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

print("CSV file created successfully.")