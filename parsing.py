#parsing html content using beatiful soup
import requests
from bs4 import BeautifulSoup

url= "https://score808.us"
r=requests.get(url)


soup  = BeautifulSoup(r.text,"lxml")
print(soup.div)