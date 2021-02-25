from bs4 import BeautifulSoup as bs
import requests
import os

# location = input('Enter location')
link = f"https://www.google.com/travel/hotels/Bhubaneswar?g2lb=2502548%2C2503781%2C4258168%2C4270442%2C4306835%2C4308226" \
       f"%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4463666%2C4482194%2C4482438%2C4486153%2C4491350%2C4495816%" \
       f"2C4504283%2C4270859%2C4284970%2C4291517&hl=en-IN&gl=in&ap=EgAwA2gB&q=hotels%20in%20bhubaneswar&rp=EL6UyOLs5vfPQ" \
       f"RDotoKJvc_3vPQBELHWl5u8lMHO0AEQiNvdjujJnZRrOAFAAEgCogETQmh1YmFuZXN3YXIsIE9kaXNoYQ&ictx=1&sa=X&utm_campaign=shar" \
       f"ing&utm_medium=link&utm_source=htls&ts=CAESABo3ChkSFToTQmh1YmFuZXN3YXIsIE9kaXNoYRoAEhoSFAoHCOUPEAIYGRIHCOUPEAIY" \
       f"GhgBMgIQACoPCgsoAUoCIAE6A0lOUhoA&ved=0CAAQ5JsGahcKEwiQ6qvDt4TvAhUAAAAAHQAAAAAQfw"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}

source = requests.get(link, headers=headers).text

######### enire website #########
soup = bs(source, 'lxml')
# print(soup.prettify())

##### Hotel  #####
hotel_names = soup.find_all('h2', class_='BgYkof ogfYpf ykx2he')
for names in hotel_names:
    print(names.text)

#### RATING #####
ratings = soup.find_all('span', class_='NPG4zc')
for rating in ratings:
    print(rating.span.text)

#### Num of revioew ####
num_reviews = soup.find_all('span', class_='sSHqwe uTUoTb XLC8M')
for review in num_reviews:
    print(review.text)
