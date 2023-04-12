import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect('PycharmProjects/CurrentTerm/Week4/bases/geo_stat.sqlite')

cur = con.cursor()

cur.execute("select * from geo_stat")