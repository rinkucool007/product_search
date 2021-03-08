import requests
from bs4 import BeautifulSoup

def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    #print(page.status_code)
    return page.content

def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("button", {"class": "btn btn-disabled btn-lg btn-block add-to-cart-button"})  # <--- change "text" to div
    #print(out_of_stock_divs)
    return len(out_of_stock_divs) != 0
    #return out_of_stock_div.text == "Sold Out"

def check_inventory():
    url = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        print("Out of stock")
    else:
        print("In Stock")

check_inventory()
