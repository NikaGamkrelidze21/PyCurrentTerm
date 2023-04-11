import sqlite3
from pprint import pprint

conn = sqlite3.connect("PycharmProjects/CurrentTerm/Week4/bases/book_db.sqlite")
cur = conn.cursor()

# task N1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def find_shakespeare():
    data = cur.execute("select title from books WHERE author='William Shakespeare'")
    return data.fetchall()

def find_shakespeare_or_rowling():
    data = cur.execute(
        """select title from books 
        WHERE   author='William Shakespeare' 
                OR  author='Rowling'""")
    return data.fetchall()

def price_condition_lower_then(price):
    data = cur.execute("""select title from books where price < :pr""",{"pr":price})
    return data.fetchall()

def unique_authors():
    data = cur.execute("""select distinct author from books""")
    return data.fetchall()
    
def users_have_money_more_then(money):
    data = cur.execute("""select username from users
                       where balance > :money""", {"money":money})
    return data.fetchall()

def users_have_bought_book():
    data = cur.execute("""select username from users
                       where id in (select distinct user_id from purchase)""")
    return data.fetchall()
    
def book_ever_sold():
    data = cur.execute("""select * from books
                       where id in (select distinct book_id from purchase)""")
    return data.fetchall()
    
def book_never_sold():
    data = cur.execute("""select title from books
                       where id not in (select distinct book_id from purchase)""")
    return data.fetchall()

def users_and_books_they_bought():
    data = cur.execute("""select u.username, p.book_id 
                       from users as u inner join purchase p 
                       on u.id = p.user_id """)
    return data.fetchall()
    

    
    
    
    
def test_all(*args):
    for index, arg in enumerate(args):
        print("- "*30)
        print(f"Query N{index+1}")
        pprint(arg)
        print("- "*30 +"\n")

test_all(
        find_shakespeare(),
        find_shakespeare_or_rowling(),
        price_condition_lower_then("20"),
        unique_authors(),
        users_have_money_more_then(100),
        users_have_bought_book(),
        book_ever_sold(),
        book_never_sold(),
        users_and_books_they_bought(),
        )