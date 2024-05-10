#parsing html content using beatiful soup
import requests
from bs4 import BeautifulSoup

url= "https://www.tuko.co.ke/"
r=requests.get(url)


soup  = BeautifulSoup(r.text,"lxml")
print(soup.title)