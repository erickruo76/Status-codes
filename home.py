import requests

url="https://www.tuko.co.ke"
rl=requests.get(url)
print(rl.status_code)