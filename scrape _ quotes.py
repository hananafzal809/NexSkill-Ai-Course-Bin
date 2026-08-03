import requests
from bs4 import BeautifulSoup
import csv

url = "https://passiton.com/inspirational-quotes"


response = BeautifulSoup.get(url)
soup= BeautifulSoup(response.text, "html.parser")


quote_divs = soup.find_all("div", class_="text-center mb-8")

print(f"Total {len(quote_divs)} quotes mile\n")

for i, div in enumerate(quote_divs, 1):
     quote_text = div.get_text(separator=" ", strip=True)
    
     print(f"Quote {i}: {quote_text}")
     print("-" * 50)
quote = soup.find ("p",class_= "darkgrid").get_text ()
author = soup.find("p",class_= "darkgrid/50").get_text()  ="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://cdn.passiton.com/quotes/images/7580/20260729_wednesday_quote.jpg" width="445" height="593">