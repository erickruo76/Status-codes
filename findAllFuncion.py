import requests
from bs4 import BeautifulSoup

url= "https://www.livescore.com/en/news/arsenal-beat-man-utd-to-put-title-race-pressure-back-on-man-city-2024051217390064438/"

r=requests.get(url)

desc= BeautifulSoup(r.text,"lxml")

elements= desc.find_all("div",{"class":"Kh Nh"})

for element in elements:
    #print(element.text.strip())


        df = elements.DataFrame()
print(df)

