

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests

print("ENTER YOUR SEARCH")
input_=input()
url = 'https://google.com/search?q={} wikipedia'.format(input_)
driver = webdriver.Chrome(executable_path="enter the path to Chromedriver on your system")
driver.get(url)
html = bs(driver.page_source, "html.parser")

div = html.find('div', {'class': 'g'})
link=div.a.get("href")


site=requests.get(link)
soup=bs(site.text,"html.parser")
result=soup.find(id="mw-content-text")
para=result.findAll("p")
data=[]
lis=para[2].text
lis1=para[3].text
print(lis)
print(lis1)
print(""" \n\n NOTE:
IF YOURE DESIRED SEARCH IS NOT FOUND ON WIKIPEDIA THE THIS PROGRAM RETURNS THE FIRST WIKIPEDIA RESULT FROM GOOGLE SEARCH""")


