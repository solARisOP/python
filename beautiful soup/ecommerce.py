import requests as re
from bs4 import BeautifulSoup
url = "https://www.amazon.in/s?k=iphone&crid=ZP14V3NAVK51&sprefix=%2Caps%2C370&ref=nb_sb_ss_recent_1_0_recent"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# proxies ={
#     "http" : "http://scraperapi:cec67b22d8aadf18c6cbd4c90013025e@proxy-server.scraperapi.com:8001",
#     "https" : "http://scraperapi:cec67b22d8aadf18c6cbd4c90013025e@proxy-server.scraperapi.com:8001",
# }
def fetchandsavetofile(url, path):
    r = re.get(url, headers=headers)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)
        
fetchandsavetofile(url, "data/ecom.html")

