import requests as re
from bs4 import BeautifulSoup

with open("data/ecom.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")

for span in spans:
    print(span.string)


prices = soup.select("span.a-price")

for price in prices:
    if not "a-text-price" in price.get("class"):
        print(price.find("span").get_text().split('¹')[1])