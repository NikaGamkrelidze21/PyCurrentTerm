import requests
import json
import http.client

def Get_languages():
    # ამ ფუნქციით ვამოწმებ api რომელსაც ვხმარობ რა 
    # ენებს ასაფორთებს ვიმახსოვრებ ლისტში რომ 
    # შემდეგ ამ ენებს გადავუარო და ყველა
    # შესაძლო ენაზე ვათარგმნინო უპარამეტრო
    conn = http.client.HTTPSConnection("microsoft-translator-text.p.rapidapi.com")

    headers = {
    'X-RapidAPI-Key': "c0be979cd8msh4bfef5909f49b03p105516jsn0792c3c189d0",
    'X-RapidAPI-Host': "microsoft-translator-text.p.rapidapi.com"
    }

    conn.request("GET", "/languages?api-version=3.0", headers=headers)

    res = conn.getresponse()
    data = res.read()
    dict_ = json.loads(data)
    languages = dict_['translation']
    return languages

def Translate(text='Happy birthday', to_language='es'):
    # ეს ფუნქცია კი უშუალოდ api-ის დახმარებით
    # მითარგმნის ტექსტს სხვადასხვა ენაზე გადაეცემა 
    # 2 პარამეტრი ტექსტი რომელიც უნდა ითარგმნოს 
    # და ენა რომელზეც უნდა გადავთარგმნო
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
    querystring = {
        "to[0]":to_language,
        "api-version":"3.0"
        }
    payload = [{ "Text": text }]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "c0be979cd8msh4bfef5909f49b03p105516jsn0792c3c189d0",
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    return response.json()


