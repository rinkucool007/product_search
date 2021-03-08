import requests
from bs4 import BeautifulSoup

url = "https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html?condition=New"
#url = "https://www.gamestop.com/video-games/playstation-5/accessories/products/sony-dualsense-wireless-controller/11106262.html?rrec=true"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

addToCartButton = soup.find('button', class_='add-to-cart btn btn-primary')
availability = str(addToCartButton)
button = str(addToCartButton).split(',')#a list of the buttons components
print(button[10][16:-1])#prints the result of availability
