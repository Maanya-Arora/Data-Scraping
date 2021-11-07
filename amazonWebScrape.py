import csv
from bs4 import BeautifulSoup

# install chromium, its driver, and selenium
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
!pip install selenium
# set options to be headless, ..
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# open it, go to a website, and get results
wd = webdriver.Chrome('chromedriver',options=options)


#obtaining search term
searchterm = input("enter your search term:")
def get_url(search_term):
  "generate a URL from the search term"
  search_term = search_term.replace(" ", "+")
  template = f"https://www.amazon.com/s?k={search_term}&ref=nb_sb_noss_2"
  return template
url = get_url(searchterm)
wd.get(url)

#creating parser: soup
soup = BeautifulSoup(wd.page_source, "html.parser")
results = soup.find_all('div', {'data-component-type':'s-search-result'})

#first item
item = results[0]

#creating records
def extractrecords(item):
  atag = item.h2.a
  description = atag.text.strip()
  url = "https://www.amazon.com" + atag.get('href')

  try:
    priceparent = item.find('span','a-price')
    priceparent.find('span','a-offscreen')
    price = priceparent.find('span','a-offscreen').text
  except AttributeError:
    return

  try:
    rating = item.i.text
    reviewcount = item.find('span','a-size-base').text
  except AttributeError:
    rating = ""
    reviewcount = ""
  if rating:
    rating = rating.split()[0]

  result = (description, url, price, rating, reviewcount)
  return result

records = []
results = soup.find_all('div', {'data-component-type':'s-search-result'})

for item in results:
  records.append(extractrecords(item))

#records for all pages
def get_url(search_term, page):
  "generate a URL from the search term"
  search_term = search_term.replace(" ", "+")
  template = f"https://www.amazon.com/s?k={search_term}&page={page}&ref=nb_sb_noss_2"
  return template

page = soup.find_all("li","a-disabled")[-1].text

records = []
for i in range(int(page)):
  url = get_url(searchterm, i+1)
  #print(url)

  wd.get(url)
  soup = BeautifulSoup(wd.page_source, "html.parser")
  results = soup.find_all('div', {'data-component-type':'s-search-result'})

  for item in results:
    records.append(extractrecords(item))

wd.close()

#save data to a csv
with open('amazonwebscrape.csv','w',newline = '', encoding='utf-8') as f:
  writer = csv.writer(f)
  writer.writerow(['description','url','price','rating','reviewcount'])
  writer.writerows(records)
