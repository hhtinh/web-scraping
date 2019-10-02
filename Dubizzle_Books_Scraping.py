from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd

base_url = "https://uae.dubizzle.com/classified/"
base_category = "books/"
links = []
domain = urlparse(base_url).scheme+"://"+urlparse(base_url).netloc

# required fields
titles = []
listing_url = []
listing_date = []
age = []
usage = []
condition = []

# optional fields
description = []
phone = []

def browseCategory(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find(id="show").findAll("a"):
        if url+link.attrs['href'] not in links:
            links.append(url+link.attrs["href"])
            
def getRequiredData(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
      
    # feature item
    feature = bsObj.find(id="featured-content")
    titles.append(feature.find("h3").find("a").text.strip())
    listing_url.append(feature.find("h3").find("a").attrs["href"])
      
    rows = feature.find("ul", {"class":"featured_listing_featurelist"}).findAll("strong", {"class":"cell"})
    age.append(rows[0].text.strip())
    usage.append(rows[1].text.strip())
    condition.append(rows[2].text.strip())
      
    bottom = bsObj.find(id="featured-listings").find("div",{"class":"datefield cols"})
    date = bottom.find("span", {"class":"date"}).text
    date += " "+bottom.find("span", {"class":"month-year"}).text
    listing_date.append(dt.datetime.strptime(date, "%d %B %Y").strftime("%Y-%m-%d"))
      
    # listing items
    for title in bsObj.findAll(id="title"):
        title_url = title.find("span", {"class":"title"}).find("a")
        titles.append(title_url.text.strip())
        listing_url.append(title_url.attrs["href"])
    
    for desc in bsObj.find(id="results-list").findAll("div", {"class":"description"}):
        rows = desc.findAll("strong")
        age.append(rows[0].text.strip())
        usage.append(rows[1].text.strip())
        condition.append(rows[2].text.strip())
        date = desc.find("p", {"class":"date"})
        listing_date.append(dt.datetime.strptime(date.text, "%d %B %Y").strftime("%Y-%m-%d"))
    
    # next page
    next = bsObj.find("div", {"class":"pagingarea"}).find(id="next_page")
    if next is not None:
        getRequiredData(domain+next.attrs["href"])
    
# MAIN

html = urlopen(base_url+base_category)
bsObj = BeautifulSoup(html, "html.parser")
for link in bsObj.find(id="show").findAll("a"):
    browseCategory(base_url+base_category+link.attrs["href"])

for url in links:
    #print(url)
    getRequiredData(url)

# Use dataframe to output CSV file

df = pd.DataFrame(titles, columns=["title"])
df["listing_url"] = listing_url
df["listing_date"] = listing_date
df["age"] = age
df["usage"] = usage
df["condition"] = condition

df.to_csv("Dubizzle_Books_Scraping.csv")
