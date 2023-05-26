import requests
from twilio.rest import Client
from pprint import pprint
import sys
sys.path.append("..")
from translate import Translate
from messengerapi import SendApi
import vonage
import plivo    


twilio_acc_sid = "AC648a156ee4e8d02b8cf0704e50f7db3f"
twilio_auth_tocken = "89e75e6c479d701160ec193b2d65a30f"
my_phone_number = "+995598247477"
  
# not working properly
def Send_sms(to=my_phone_number, sms = 'Testing'):

    client = Client(twilio_acc_sid, twilio_auth_tocken)

    message = client.messages.create(
        body= sms ,
        from_="+13156421892",
        to= to
    )

    print(message.sid)
    
# not working properly
def Send_Messenger(message="Hello World", recipient_id="nika.gamkrelidze.509"):
    send_api = SendApi("EAAKgJUu3ULYBANZBZC6Azl9lZBe0UaLEVkfb5okY0blK7nCZBAzXVv2Q98NEcdSgM6ZCZCI1lq4YfZAg74a8VZALBzIYeqGiA6ZCk5OiQr9YaKTmex40rgFtogcpZCbWZAY7ligKLhkZBaRtbjexy73ZCnfvhAOVLfLVqluxVtgngjW97ZCV40AKuFqXJwGZA1PsMX1UMx6zZAQ1PuZAJfQedS0ej9F6XejH4tcfZBYsK0zxIOmK88X7o9L279Qanl")
    send_api.send_text_message(message=message, recipient_id=recipient_id)

# not working properly
def send_Vonage():
    client = vonage.Client(key="d2f8c6ed", secret="6RTHYlsGIVzR0bWP")
    sms = vonage.Sms(client)
    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "995571078246",
            "text": "Happy birthday MAgd \n\n\n",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

# not working properly
def send_Plivo():
    client = plivo.RestClient('<auth_id>','<auth_token>')
    response = client.messages.create(
        src='995598247477',
        dst='995571078246',
        text='Hello, this is sample text',
        url='https://<yourdomain>.com/sms_status/',
        )
    print(response)
    #prints only the message_uuid
    print(response.message_uuid)

# WORKS
def send_Courier():
    url = "https://api.courier.com/send"
    payload = {
    "message": {
        "content": {
        "body": "Happy Birthday Darling",
        "title": "Happy Birthday"
        },
        "to": {
        "email": "nika.gamkrelidze.1@btu.edu.ge"
        }
    }
    }
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer pk_prod_PRXVFK9T3H4CXXHZRMTBGQV6BRMK"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)


