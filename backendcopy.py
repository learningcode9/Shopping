import psycopg2


def connect():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS shopping (productid TEXT PRIMARY KEY,onlinefrom text,onlineto text,amount text,priceinfo text)")
    conn.commit()
    conn.close()
def insert(productid,onlinefrom,onlineto,amount,priceinfo):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO shopping VALUES (%s,%s,%s,%s,%s)",(productid,onlinefrom,onlineto,amount,priceinfo))
    #cur.execute("INSERT INTO shopping (productid,onlinefrom,onlineto,amount,priceinfo), VALUES (%s,%s,%s,%s,%s)")
    conn.commit()
    conn.close()
def view():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM shopping")
    rows=cur.fetchall()
    conn.close()
    return rows
def search(productid="",onlinefrom="",onlineto="",amount="",priceinfo=""):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM shopping WHERE productid=%s OR onlinefrom=%s OR onlineto=%s OR amount=%s OR priceinfo=%s",(productid,onlinefrom,onlineto,amount,priceinfo))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(productid):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM shopping WHERE productid=%s",(productid,))
    #rows=cur.fetchall()
    conn.commit()
    conn.close()

def update(productid,onlinefrom,onlineto,amount,priceinfo):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE shopping SET onlinefrom=%s,onlineto=%s,amount=%s,priceinfo=%s WHERE productid=%s",(onlinefrom,onlineto,amount,priceinfo,productid))
    #rows=cur.fetchall()
    conn.commit()
    conn.close()


connect()
#insert('12345678','2018-10-12','2018-10-9-6','800','k34hng7')
#view()
#search()
#delete('12345678')
#update()