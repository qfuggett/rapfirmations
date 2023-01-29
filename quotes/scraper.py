import requests
from bs4 import BeautifulSoup

URL = "https://becentsational.com/best-rap-quotes/"
response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
quotes = soup.find_all("blockquote", class_="wp-block-quote")
num = 1
for quote in quotes:
    num = num + 1
    print("QUOTE", num, quote)
