import requests

url="https://www.tuko.co.ke/entertainment/celebrities/547640-king-kaka-wins-ksh-x-bet-staking-big-real-madrids-victory-bayern-munich/"
weburl=requests.get(url)
print(weburl.status_code)