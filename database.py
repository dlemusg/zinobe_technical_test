import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect(':memory:')
        print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    
    return con


def create_core_table(con):
    cursorObj = con.cursor()
    try:  
        cursorObj.execute("CREATE TABLE core(region text, country text PRIMARY KEY, language text, time real)")
        con.commit()
    except Error:
        print(Error)
    


def insert_row(entities):
    cursorObj = con.cursor()

    for entity in entities:

        try:
            region = entity['region']
            country = entity['country']
            language = entity['language']
            time = entity['time']
            cursorObj.execute('INSERT INTO core(region, country, language, time) VALUES(?, ?, ?, ?)', (region, country, language, time))
            con.commit()
        except Error:
            print(Error)
    

def sql_fetch(con):

    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM core')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)




con = sql_connection()
create_core_table(con)