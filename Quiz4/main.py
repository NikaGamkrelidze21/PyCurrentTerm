import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import csv
import base64
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import requests
from io import BytesIO

sorted_data = []
page = 1
payload = {
    's' : "tarot",
    'post_type' : 'product',
    'per_page' : '24',
    'Accept-Language': 'en-US'

}

try:
    while True:
        url = f'https://onlinetarot.ge/shop/page/{page}/'

        response = requests.get(url, payload, )

        print(response.status_code)
        if response.status_code == 404:
            raise Exception('Pages Out of Range')

        data = response.text

        # print(data)

        soup = BeautifulSoup(data, 'html.parser')


        products = soup.find('div', class_='products').find_all('div', class_='product-wrapper')


        def Get_image(url):
            resp = requests.get(url).content
            image_base64 = base64.b64encode(resp)
            return image_base64

        for index, product in enumerate(products):
            temp_dict = {}
            
            temp_dict['title'] = product.h3.text
            temp_dict['price'] = product.bdi.text
            temp_dict['url'] = product.h3.a['href']
            temp_dict['img_url'] = product.picture.img['src']
            
            # Comming Soon
            # temp_dict['img'] = Get_image(temp_dict['img_url'])
            # print(temp_dict['img'])
            
            sorted_data.append(temp_dict)
        print('parsed Page:', page)
        page += 1
        time.sleep(5)
except:
    print('Stopped Before Page N', + page)

with open('Uni/PycharmProjects/CurrentTerm/Quiz4/tarot.csv', 'w', encoding='UTF-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(('ID', 'Title', 'Price', 'Image URL', 'URL'))
    
    for index, i in enumerate(sorted_data):
        writer.writerow((index, i['title'], i['price'], i['img_url'], i['url']))  
