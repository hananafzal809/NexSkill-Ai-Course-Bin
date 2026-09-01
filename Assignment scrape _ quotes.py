import requests
from bs4 import BeautifulSoup
import csv

url = "https://passiton.com/inspirational-quotes"


response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")


quote_divs = soup.find_all("div", class_="text-center mb-8")

print(f"Total {len(quote_divs)} quotes mile\n")

for i, div in enumerate(quote_divs, 1):
     quote_text = div.get_text(separator=" ", strip=True)
    
     print(f"Quote {i}: {quote_text}")
     print("-" * 50)
 
  