# class Person:
#     def __init__(self, name, deposit=1000, loan=0):
#         self.name = name
#         self.deposit = deposit
#         self.loan = loan
#
#     def __str__(self):
#         return f"სახელი - {self.name}\n დეპოზიტი - {self.deposit}\n სესხი - {self.loan}\n"
#
#
# class Hause:
#     def __init__(self, ID, price, owner, status="გასაყიდი"):
#         self.ID = ID
#         self.price = price
#         self.status = status
#         self.owner = owner
#
#     def sell(self, buyer, loan=None):
#         self.owner.deposit += self.price
#         self.owner = buyer
#         if loan is not None:
#             buyer.loan += loan
#             buyer.deposit -= self.price-loan
#             self.status = "გაყიდულია სესხით "
#             return f"{buyer.name}-მა სესხით შეისყიდა სახლი აიდით-{self.ID}"
#         else:
#             self.status = "გაყიდულია"
#             buyer.deposit -= self.price
#             print(f"{self.owner.name}-მა შეისყიდა სახლი აიდით-{self.ID}")
#
#
#
# p1 = Person('Luka', 4000)
# p2 = Person('Giorgi', 300000, 2000)
# h1 = Hause('fd24', 200000, p1)
# # h1.sell(p2)
# h1.sell(p2, 30000)
#
# print(p1)
# print(p2)




import sqlite3
conn = sqlite3.connect('db_books.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS books
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(30),
            author VARCHAR(30),
            price FLOAT)
''')


b_title = 'ლექსების კრებული'
b_author = 'ვაჟა'
b_price = 10
book_item = (b_title, b_author, b_price)



# cur.execute("INSERT INTO books (title, author, price) VALUES  ('კაცია-ადამიანი?!', 'ილია ჭავჭავაძე', 15)")
# cur.execute(f"INSERT INTO books (title, author, price) VALUES  ('{b_title}', '{b_author}', {b_price})")
# cur.execute("INSERT INTO books (title, author, price) VALUES  (?, ?, ?)", (b_title, b_author, b_price))
# cur.execute("INSERT INTO books (title, author, price) VALUES  (?, ?, ?)", book_item)



book_list = [
            ('The Book Thief', 'Markus Zusak', 17),
            ('Animal Farm', 'George Orwell', 13),
            ('The Hunger Games', 'Suzanne Collins', 17),
            ('Harry Potter and the Prisoner of Azkaban', 'Rowling',  25),
            ('Harry Potter and the Goblet of Fire', 'Rowling', 24),
            ('გამზრდელი', 'აკაკი წერეთელი', 8),
            ('ჩემი თავგადასავალი', 'აკაკი წერეთელი', 8),
            ('განდეგილი', 'ილია ჭავჭავაძე', 10),
            ('ვეფხისტყაოსანი', 'შოთა რუსთაველი', 29)
        ]

cur.executemany("INSERT INTO books (title, author, price) VALUES  (?, ?, ?)", book_list)

conn.commit()
conn.close()



