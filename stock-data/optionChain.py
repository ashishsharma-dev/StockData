import requests
import pandas as pd

URL = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.7"
}

session = requests.Session()
request = session.get(URL, headers=headers)
cookies = dict(request.cookies)

response = session.get(URL, headers=headers, cookies=cookies).json()

rawdata = pd.DataFrame(response)
print(len(rawdata['records']['data']))