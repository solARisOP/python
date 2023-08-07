import requests as re

def fetchandsavetofile(url, path):
    r = re.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)


url = "https://timesofindia.indiatimes.com/india/nitin-gadkari-for-doubling-agriculture-share-in-gdp-to-achieve-higher-economic-growth-says-modi-govt-focussed-on-rural-sectors/articleshow/100676883.cms"

fetchandsavetofile(url, "data/times1.html")