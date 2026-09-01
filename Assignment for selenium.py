from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://www.values.com/inspirational-quotes"

s = webdriver.ChromeService(executable_path="C:\\Users\Hp\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe") #'/Users/bpfalz/Downloads/chromedriver' for my macbook
driver = webdriver.Chrome(service=Service)

driver.get(url)

quoteList = []
quotesDiv = driver.find_elements(By.XPATH, "//div[contains(@class, 'text-center mb-8')]")

for p in range(len(quotesDiv) - 1):
    quote = {}
    innerImg = quotesDiv[p+1].find_element(By.TAG_NAME, "img")
    innera = quotesDiv[p+1].find_element(By.TAG_NAME, "a")
    
    quote["img"] = innerImg.get_attribute('src')
    quote["lines"] = innerImg.get_attribute('alt')
    quote["url"] = innera.get_attribute('href')
    
    quoteList.append(quote)

print(quoteList)
