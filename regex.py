import requests
from bs4 import BeautifulSoup
import re

url = "https://www.livescore.com/en/news/arsenal-beat-man-utd-to-put-title-race-pressure-back-on-man-city-2024051217390064438/"

r = requests.get(url)

desc = BeautifulSoup(r.text, "html.parser")

# Find all paragraphs containing the word "Arsenal"
paragraphs = desc.find_all(string=re.compile("Arsenal"))

print(len(paragraphs))
for paragraph in paragraphs:
    print(paragraph.text.strip())
