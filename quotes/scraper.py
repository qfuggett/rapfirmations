import re
import requests
from bs4 import BeautifulSoup

def scrape_quote() -> list:
    URL = "https://becentsational.com/best-rap-quotes/"
    response = requests.get(URL)

    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all("blockquote", class_="wp-block-quote")
    num = 0

    for quote in quotes:
        num = num + 1
        split = quote.text
        author_split = re.split('[—―–]', split)
        author = author_split[-1]
        quote = author_split[0]
        print(num, "By", author, ":", quote)

        return [author, quote]
