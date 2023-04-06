import sqlite3

conn = sqlite3.connect("test_database.sqlite")
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS   books
               (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title VARCHAR(30),
                   author VARCHAR(30),
                   price FLOAT
               )
               
               ''')
b_title = 'ლექსების კრებული'
b_author = 'ვაჟა'
b_price = 10

book_item = (b_title, b_author, b_price)


cursor.execute("INSERT INTO books (title, author, price) VALUES  ('კაცია-ადამიანი?!', 'ილია ჭავჭავაძე', 15)")
cursor.execute(f"INSERT INTO books (title, author, price) VALUES  ('{b_title}', '{b_author}', {b_price})")
cursor.execute("INSERT INTO books (title, author, price) VALUES  (?, ?, ?)", (b_title, b_author, b_price))
cursor.execute(f"INSERT INTO books (title, author, price) VALUES  ({b_title},{b_author},{b_price})")


conn.commit()
conn.close()