import sys
sys.path.append('..')
import email_sender
import translate
from datetime import date
import time


# ცაწერეთ დაბადების თვე და რიცხვი
# მიზანია რომ აქ მითითებული რიცხვი თუ არ არის დღეს 
# არ გააგზავნის მილოცვებს, თუ გსურთ გატესტოთ პროგრამა 
# მიუთითეთ დღევანდელი თარიღი იგივე ფორმატით mm-dd 
Birthday_Date = '05-21'

# მეილი რომელზეც უნდა მივიდეს მილოცვები
Recipient_Email = 'nika.gamkrelidze.1@btu.edu.ge'

# მისალოცი ტექსტი (აუცილებელია იყოს ინგლისურად)
congratulation_Text = 'Happy Birthday Nika'


def __main__():
    languages = [ i for i in translate.Get_languages()]
    
    for index, language in enumerate(languages):
        tranlsation = translate.Translate(congratulation_Text, language)
        text = tranlsation[0]['translations'][0]['text']
        lang = tranlsation[0]['translations'][0]['to']

        email_sender.send_Email(Recipient_Email,lang,text)
        
        # ლოგს ვაკეთებ რომ დავაკვირდეთ რომელ იტერაციაზე ვარ
        print('- ' * 20)
        print(f'CONSLE LOG\nAttempt N{index+1} \nSMS HAS BEEN SENT:',text, '\n', 'On Language:', lang, '\n', 'TO:', Recipient_Email)
        
        # ვაძინებ პროგრამას რომ ყოველი გაგზავნის 
        # შემდეგ 1 წუთი მოიცადოს სანამ ხელახლა
        # გადათარგმნის და გააგზავნის მილოცვას
        time.sleep(60)

while str(date.today())[5:] == Birthday_Date:
    __main__()