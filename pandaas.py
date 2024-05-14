import pandas as pd
import requests
from bs4 import BeautifulSoup

url= "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")


product_names = []

for name in soup.find_all("a", class_="title"):
    product_names.append(name.text)
print(product_names)


prices = soup.find_all("h4", class_="price float-end card-title pull-right")

product_prices = []

for i in prices:
    namee = i.text
    product_prices.append(namee)
    
#print(product_prices)


desc = soup.find_all("p", class_="description card-text")

product_desc = []

for i in desc:
    des = i.text
    product_desc.append(des)
    
#print(product_desc)



rev = soup.find_all("p", class_="review-count float-end")

product_rev = []

for i in rev:
    revv = i.text
    product_rev.append(revv)
    
#print(product_rev)


df= pd.DataFrame({"Product Name":product_names,"Prices":product_prices,
                  "Description":product_desc,"Product Reviews":product_rev})

df.to_excel("Product.xlsx")

