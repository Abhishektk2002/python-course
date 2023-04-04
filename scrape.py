import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.cet.ac.in/head-of-departments/")
source = req.content
soup = BeautifulSoup(source,"lxml")
figure = soup.find("figure",class_="wp-block-table")
table = figure.find("table")
table_rows = table.find_all("tr")
table_rows = table_rows[1:]
for row in table_rows:
    tds = row.find_all("td")
    n = tds[0].text
    m = tds[1].text
    s = tds[2].text
    print(n,m,s)