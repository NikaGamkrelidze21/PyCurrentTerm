import requests

def send_Email(email = "nika.gamkrelidze.1@btu.edu.ge", title="Happy Birthday",  text = "Happy Birthday Darling"):
    # გადაეცემა 3 ატრიბუტი მეილი რომელზეც უნდა გაიგზავნოს 
    # მილოცვა, სათაური რომელიც გამოცნდება მეილის აღწერაში 
    # ტექსტი რომელიც უშუალოდ მეილში იქნება ცაწერილი
    # api.courier ის დახმარებით ვაგზავნი მეილზე ტექსტს
    
    url = "https://api.courier.com/send"
    
    payload = {
        "message": {
            "content": {
            "body": text,
            "title": title
            },
            "to": {
            "email": email
            }
        }   
    }
    
    # თუ გინდათ თქვენი მეილიდან იყოს გაგზავნილი მილოცვა 
    # უნდა გადახვიდეთ https://www.courier.com/ დარეგისტრირდეთ
    # და თქვენი api key დააგენერიროთ რომელსაც ჩასვამთ "Authorization"-ში 
    # ქვემოთ მოცემული ფორმატით "Bearer " + api_key
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer pk_prod_PRXVFK9T3H4CXXHZRMTBGQV6BRMK"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return (response.text)

