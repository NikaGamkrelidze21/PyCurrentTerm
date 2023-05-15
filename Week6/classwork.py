import requests
from pprint import pprint
import json

# response = requests.get('https://google.com')

# pprint(response.content)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# image_url = "https://cdn.gweb.ge/buffer/1001285/pictures/slider/7555b47f7d4683e3dd002dc0b18c2ec4.png"

# response = requests.get(image_url)

# photo = response.content

# with open("image.png", "wb") as file :
#     file.write(photo)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

key = "887aaff89bee4fd742287bfd4afa2483"
city = "Tbilisi"
resp0 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={'Tbilisi'},&limit={5}&appid={key}")
text = resp0.text
json_data = json.loads(text)

lat = (json_data[0]['lat'])
lon = json_data[0]['lon']
code = json_data[0]['country']

# print(lat, lon, code)

# resp = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric').text 

# resp_structured = json.dumps(json.loads(resp))

# main = json.loads(resp)['main']

# print(main['humidity'])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

key = "887aaff89bee4fd742287bfd4afa2483"
url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={key}"

response = requests.get(url)
result = response.text
data = (json.loads(result))
list_ = data['list']
components = list_[0]['components']
pprint(components)