#code trial selenium adsp

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open ADSP datasets page
url = "https://dss.niagads.org/datasets/"
driver.get(url)

# Allow page to load
time.sleep(3)

# website has infinite scroll so need time for everything to load properly
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Let new content load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# scroll is done so now dataset can be extracted
dataset_cards = driver.find_elements(By.CLASS_NAME, "dataset-section")

# extracting all dataset info
for card in dataset_cards:
        title_elem = card.find_element(By.CLASS_NAME, "dataset-section-title")
        link_elem = title_elem.find_element(By.TAG_NAME, "a")
        access_elem = card.find_element(By.CLASS_NAME, "acces-icon-area")
        access_text = access_elem.find_element(By.TAG_NAME, "span")
        desc_elem = card.find_element(By.CLASS_NAME, "dataset-description-area")
    
    
        title = title_elem.text.strip()
        link = link_elem.get_attribute("href").strip()
        access = access_text.text.strip()
        description = desc_elem.text.strip()
        

        print(f"Title: {title}")
        print(f"Access: {access}")
        print(f"Description: {description}")
        print(f"Link: {link}")
        print("-" * 60)


# shutting the browser
driver.quit()

