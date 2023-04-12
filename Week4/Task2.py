import sqlite3
from pprint import pprint
con = sqlite3.connect("PycharmProjects/CurrentTerm/Week4/bases/Titanic.sqlite")
cur = con.cursor()

def percentage_by_sex(sex):
    selected_amount = cur.execute(f"""select count(name) from passengers 
                where sex = '{sex}'""").fetchall()
    
    total_amount = cur.execute("""select count(name) from passengers""").fetchall()
    percentage = selected_amount[0][0] / total_amount[0][0] *100
    return (f'{sex} percentage is {percentage:.2f}%')

def survived_by_sex(survived,sex):
    selected_amount = cur.execute(f"""select count(name) from passengers 
                where sex = '{sex}' and survived ='{survived}' """).fetchall()
    
    total_amount = cur.execute("""select count(name) from passengers""").fetchall()
    percentage = selected_amount[0][0]
    return (f'{sex} survived {selected_amount[0][0]}')
    
def ticket_class(lvl):
    passengers = cur.execute(f"""select count(passengerid) from passengers 
                             where Pclass = {lvl}
                             """).fetchall()
    return passengers[0][0]

def avg_ticket_price(lvl):
    avg_price = cur.execute(f"""select avg(fare) from passengers 
                             where Pclass = {lvl}
                             """).fetchall()
    return avg_price[0][0]
    
    
def execute_all(*args):
    for index, arg in enumerate(args):
        print("- "*30)
        print(f"Query N{index+1}")
        pprint(arg)
        print("- "*30 + "\n")


execute_all(
    percentage_by_sex('female'),
    percentage_by_sex('male'),
    survived_by_sex(0,'female'),
    survived_by_sex(0,'male'),
    survived_by_sex(1,'female'),
    survived_by_sex(1,'male'),
    ticket_class(1),
    ticket_class(2),
    ticket_class(3),
    avg_ticket_price(1)
    
    )
