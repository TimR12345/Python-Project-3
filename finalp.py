#Timothy Rohe
#Gas price Locater


#I will be using Beautiful Soup to find the prices
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

url = 'https://gasprices.aaa.com/?state=NJ'
#this method I found that would allow me to actually acces
#the data and not give me an error
req = Request(url, headers = {'User-Agent' : 'Mozilla/5.0'})

webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
#the data I want is contained in a table element

table = page_soup.find("table")
print(table)
