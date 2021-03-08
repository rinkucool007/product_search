from bs4 import BeautifulSoup
import requests

def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content

def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("img", {"class": "oos-overlay hide"})
    #out_of_stock_divs = soup.findAll("img", {"class": "product-out-stock-overlay"})
    return len(out_of_stock_divs) != 0

def check_inventory():
    url = "https://www.costco.com/CatalogSearch?dept=All&keyword=ps5+console"
   #url = "https://www.costco.com/.product.100714322.html?ADBUTLERID=large_ad_microsoft"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        print("In stock")
    else:
        print("Out of stock still")

check_inventory()
