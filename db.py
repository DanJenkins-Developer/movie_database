import sqlite3
from contextlib import closing

def create(path):

    conn = sqlite3.connect(path)
    return conn

def read(conn, query):
    
    results = 0
    cur = conn.cursor()

    with closing(cur) as c:
        c.execute(query)
        results = c.fetchall()

    return results

def delete(conn, delete_query):

    cur = conn.cursor()
    cur.execute(delete_query)
    conn.commit()

def insert(conn, insert_query):

    cur = conn.cursor()
    cur.execute(insert_query)
    conn.commit()





