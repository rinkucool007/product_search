import requests
from bs4 import BeautifulSoup

def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    #print(page.status_code)
    return page.content

def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_div = soup.find("div", {"class": "product-inventory"})
    return out_of_stock_div.text == "In stock."

def check_inventory():
    url = "https://www.newegg.com/p/N82E16868110292?Description=ps5%20console&cm_re=ps5_console-_-68-110-292-_-Product"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        print("In stock")
    else:
        print("Out of stock")

check_inventory()
