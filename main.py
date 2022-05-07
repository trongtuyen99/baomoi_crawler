import time

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://m.baomoi.com/trang1.epi")

time.sleep(5)

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, "lxml")

for link in soup.find_all(class_="bm_Cz"):
    num_related_articles = int(link.get_text().replace(" liên quan", ""))
    if 1 < num_related_articles < 30:
        print(link.get('href') + ": " + str(num_related_articles))
