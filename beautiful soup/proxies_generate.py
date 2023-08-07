import requests as re

proxies ={
    "http" : "http://scraperapi:cec67b22d8aadf18c6cbd4c90013025e@proxy-server.scraperapi.com:8001",
    "https" : "http://scraperapi:cec67b22d8aadf18c6cbd4c90013025e@proxy-server.scraperapi.com:8001",
}

r = re.get("https://api.ipify.org?format=json", proxies = proxies)
print(r.json())