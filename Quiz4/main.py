import requests
from bs4 import BeautifulSoup
import time
import csv
import base64
import requests


sorted_data = []
page = 1
payload = {
    's' : "tarot",
    'post_type' : 'product',
    'per_page' : '24',
    'Accept-Language': 'en-US'
}

def Wait(seconds):
    print('\nSleeping')
    for i in range(seconds):
        print(f'{i+1}...')
        time.sleep(1)
        
try:
    while True:
        url = f'https://onlinetarot.ge/shop/page/{page}/'

        print('\nSstarting Page N', page)
        
        response = requests.get(url, payload, )

        print(response.status_code)
        
        if response.status_code != 200:
            print('error')
            raise Exception('Pages Out of Range')

        data = response.text

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
            images = product.find_all('img', class_='attachment-woocommerce_thumbnail')
            
            for i in images:
                # საიტზე რაღაც უაზროდ აქვთ ზოგჯერ ლოგოა პირველი ზოგჯერ ტაროს ფოტო, 
                # ზოგჯერ კიდევ რაღაც სულ სხვა ლინკი და ყველა მათგანს ერთნაირი კლასი აქვთ
                # ამიტომ ყველა მომაქვს რაც დამხვდება და ვფილტრავ ლინკებს
                
                # აქ იფილტრება 404 ერორის მქონე ლინკი რადგან ყველა მათგანი იწყებოდა 'www.w3.org'-ით
                filter_eror_link= 'www.w3.org' not in str(i['src'])   
                
                # აქ იფილტრება ლოგო 
                filter_logo = 'https://onlinetarot.ge/wp-content/uploads/2022/06/images-e1656077258583.png' not in str(i['src'])
                
                # აქ ორივე ფილტრი ერთიანდება
                allow = filter_logo and filter_eror_link
                
                # აქ კი გაერთიანებულს ფილტრს გადიან ჩვენი ლინკები
                if allow: 
                    temp_dict['img_url'] = i['src'] 
                    break
            
            sorted_data.append(temp_dict)
            
        print('Scrapped Page:', page)
        page += 1
        Wait(5)
except:
    print('Stopped Before Page N', + page)

with open('Quiz4/tarot.csv', 'w', encoding='UTF-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(('ID', 'Title', 'Price', 'Image URL', 'URL'))
    
    for index, i in enumerate(sorted_data):
        writer.writerow((index, i['title'], i['price'], i['img_url'], i['url'] ))  
