import requests
import json
from pprint import pprint
from datetime import date
import openai
import os
from twilio.rest import Client


# Task1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# def Get_coordinates(city_name="Tbilisi", key = "887aaff89bee4fd742287bfd4afa2483"):
#     url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={key}"
    
#     request = requests.get(url)
#     response = request.text
#     json_response = json.loads(response)[0]
    
#     return {'city': city_name,
#             'code':json_response['country'],
#             'lon':json_response['lon'],
#             'lat':json_response['lat']}


# def Get_Air_Polution(city_data, key="887aaff89bee4fd742287bfd4afa2483"):
#     url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={city_data['lat']}&lon={city_data['lon']}&appid={key}"
    
#     request = requests.get(url)
#     response = request.text
#     json_response = json.loads(response)

#     return json_response['list'][0]['components']   
    
# Task2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# def Get_nasa_image(coordinates, dimension = 0.1, nasa_key ="U9g2dLdrTWDFqSiEq9lP6jgkIIvv2JtaOyM4QaTi"):
#     nasa_url = f"https://api.nasa.gov/planetary/earth/imagery?lon={coordinates['lon']}&lat={coordinates['lat']}&date={'2021-01-01'}&&dim={dimension}&api_key={nasa_key}"
#     request = requests.get(nasa_url)
    
#     with open('Uni/PycharmProjects/CurrentTerm/Week6/earthImage.png', 'wb') as file:
#         file.write(request.content)
    
#     return print(request)

# Get_nasa_image(Get_coordinates('Tbilisi'))

# Task3 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# sms_url = "https://getitsms-whatsapp-apis.p.rapidapi.com/45"

# querystring = {"your_number":"919876543210","your_message":"your message"}

# payload = {
# 	"your_number": "+995598247477",
# 	"your_message": "your message"
# }
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "c0be979cd8msh4bfef5909f49b03p105516jsn0792c3c189d0",
# 	"X-RapidAPI-Host": "getitsms-whatsapp-apis.p.rapidapi.com"
# }

# response = requests.post(sms_url, json=payload, headers=headers, params=querystring)

# print(response.json())



account_sid = 'AC648a156ee4e8d02b8cf0704e50f7db3f'
auth_token = '[AuthToken]'

client = Client(account_sid, auth_token)

client.messages.create(
  from_='whatsapp:+14155238886',
  body='hello',
  to='whatsapp:+995598247477'
)
