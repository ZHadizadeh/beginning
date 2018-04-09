import requests
from bs4 import BeautifulSoup

product_link = 'https://www.digikala.com/Product/DKP-354069/%DA%AF%D9%88%D8%B4%D9%8A-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-iPhone-X-%D8%B8%D8%B1%D9%81%D9%8A%D8%AA-64-%DA%AF%D9%8A%DA%AF%D8%A7%D8%A8%D8%A7%D9%8A%D8%AA'

html = requests.get(product_link).text

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')

for link in links:
    print(link)
    print(link.get("href"))
