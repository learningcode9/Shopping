import psycopg2 
from psycopg2 import Error
import backend1

connection = psycopg2.connect(user = "postgres",
                                  password = "postgres1984",
                                  host = "localhost",
                                  port = "5432",
                                  database = "postgres")
cursor = connection.cursor()


create_table_query = '''CREATE TABLE products
(
productid  TEXT ,
onlinefrom  TEXT ,
onlineto TEXT,
amount TEXT,
priceinfo TEXT 
);'''

cursor.execute(create_table_query)
connection.commit()

f = open('productsdata.csv', 'r')
cursor.copy_from(f, 'products', sep=',')
f.close()
