import requests
from bs4 import BeautifulSoup
req=requests.get("https://books.toscrape.com/")
source=req.content
soup=BeautifulSoup(source,"lxml")
article=soup.find_all("article",class_="product_pod")
for i in article:
    h3_tag=i.find("h3")
    a_tag=h3_tag.find("a")
    name=a_tag['title']
    price=i.find("p",class_="price_color")
    price=price.text
    print(name,price)
next=soup.find("li",class_="next")

