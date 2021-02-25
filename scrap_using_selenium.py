from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import csv
import time

# write location of your webdriver
driver = webdriver.Chrome('/media/mrugank/626CB0316CB002391/for development purpose only/python/web_scrapping/chromedriver_linux64/chromedriver')

url = "https://www.google.com/travel/hotels/Bhubaneswar?g2lb=2502548%2C2503781%2C4258168%2C4270442%2C4306835%2C4308226%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4463666%2C4482194%2C4482438%2C4486153%2C4491350%2C4495816%2C4504283%2C4270859%2C4284970%2C4291517&hl=en-IN&gl=in&ap=EgAwA2gB&q=hotels%20in%20bhubaneswar&rp=EL6UyOLs5vfPQRDotoKJvc_3vPQBELHWl5u8lMHO0AEQiNvdjujJnZRrOAFAAEgCogETQmh1YmFuZXN3YXIsIE9kaXNoYQ&ictx=1&sa=X&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESABo3ChkSFToTQmh1YmFuZXN3YXIsIE9kaXNoYRoAEhoSFAoHCOUPEAIYGRIHCOUPEAIYGhgBMgIQACoPCgsoAUoCIAE6A0lOUhoA&ved=0CAAQ5JsGahcKEwiQ6qvDt4TvAhUAAAAAHQAAAAAQfw"
driver.get(url)

soup = bs(driver.page_source, 'html.parser')

# I have limited scrapper to scrap details of first 5 hotel details. You can remove it and keep on scrolling in selenium to load new datas

##### Hotel  #####
hotel_names = soup.find_all('h2', class_='BgYkof ogfYpf ykx2he')[:5]

#### RATING #####
ratings = soup.find_all('span', class_='NPG4zc')[:5]

#### Num of reviews ####
num_reviews = soup.find_all('span', class_='sSHqwe uTUoTb XLC8M')[:5]

for i in range(len(hotel_names)):
    review = num_reviews[i]
    wait = WebDriverWait(driver, 10)
    review_bt = wait.until(EC.element_to_be_clickable(
                           (By.XPATH, f"//span[contains(text(),'{review.text}')]"))
                       )
    review_bt.click()
    time.sleep(3)

reviews = []

for i in range(len(hotel_names), 0, -1):
    driver.switch_to_window(driver.window_handles[i])
    soup = bs(driver.page_source, 'html.parser')
    hotel_reviews = soup.find_all('div', class_='K7oBsc')
    hotel_reviews_list = []
    for i in range(len(hotel_reviews)):
        hotel_review = str(hotel_reviews[i].div.span.text)
        try:
            if hotel_review.find(' ...') >= 0:
                hotel_review = hotel_review.replace(' ...', '')
            next_review = str(hotel_reviews[i+1].div.span.text) # sometimes detailed review is show when clicked on read more
            if next_review.find(hotel_review) >= 0:
                continue
        except:
            pass
        hotel_reviews_list.append(hotel_review)
    reviews.append(hotel_reviews_list)


#### WRITE TO CSV ####
with open('hotels.csv', mode='w') as csv_file:
    fieldnames = ['Name', 'Rating', 'Reviews']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(hotel_names)):
        hotel_reviews = reviews[i]
        review_text = '\n\n'.join(hotel_reviews)
        writer.writerow({'Name': f"{hotel_names[i].text}", 'Rating': f"{ratings[i].span.text}", 'Reviews': f"{review_text}"})
