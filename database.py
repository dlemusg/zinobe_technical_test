import sqlite3
from sqlite3 import Error



def sql_connection():
    """
    Description
    ---------
    Crea la base y establece la conexión

    Parameters
    ----------

    Returns
    -------
    Error: Conexión a la bd
    
    """
    try:
        con = sqlite3.connect('database.db')
        print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    
    return con


def create_core_table(con):
    """
    Description
    ---------
    Crea la tabla core que almacena region, pais, language y tiempo

    Parameters
    ----------
    con: Conexión a la base de datos

    Returns
    -------
    Error: En caso de error
    
    """
    cursorObj = con.cursor()
    try:  
        cursorObj.execute("CREATE TABLE core(region text, country text PRIMARY KEY, language text, time real)")
        con.commit()
    except Error:
        return Error
    


def insert_row(entities):
    """
    Description
    ---------
    Inserta los valores en un nuevo registro de la tabla

    Parameters
    ----------
    entities list: Valores a insertar en la tabla

    Returns
    -------
    Error: En caso de error
    
    """
    cursorObj = con.cursor()
    try:
        for entity in entities:
            region = entity['region']
            country = entity['country']
            language = entity['language']
            time = entity['time']
            cursorObj.execute('INSERT INTO core(region, country, language, time) VALUES(?, ?, ?, ?)', (region, country, language, time))
            con.commit()
    except Error:
        return Error
    

def sql_fetch():
    """
    Description
    ---------
    Obtiene los 5 primero registros de la tabla

    Parameters
    ----------
    
    Returns
    -------
    Error: En caso de error
    
    """
    cursorObj = con.cursor()
    try:
        cursorObj.execute('SELECT * FROM core Limit 5')
        rows = cursorObj.fetchall()
        #for row in rows:
        return rows
    except Error:
        return Error



con = sql_connection()
create_core_table(con)