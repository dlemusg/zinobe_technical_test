"""
OK ::: De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
OK ::: En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
OK ::: La tabla debe ser creada en un DataFrame con la libreria PANDAS
OK ::: Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
Guarde el resultado en sqlite.
Genere un Json de la tabla creada y guardelo como data.json
La prueba debe ser entregada en un repositorio git.
"""

import pandas as pd
import requests
import timeit
from hashlib import sha1
import json




def get_coutries_by_region(region):
    countries = requests.get(
        f'https://restcountries.com/v3.1/region/{region}').json()
    return 0


def get_all_countries():

    """
        Description
        ---------
        Obtiene la información de todos los paises expuestos en la api 

        Parameters
        ----------
        
        Returns
        -------
        tipo
            Lista de diccionarios con:
                Región: Región de pais
                Country: Nombre del pais
                Lenguaje: Idioma principal (encriptado en sha)
                Time: Tiempo que demoro la fila
    """

    countries = requests.get(f'https://restcountries.com/v3.1/all').json()

    final_countries = []

    for country in countries:
        start = timeit.timeit()
        region = country['region']

        try:
            encode_text = encode_language(
                list(country['languages'].values())[0])
        except:
            encode_text = ''

        country_text = country['name']['official']
        end = timeit.timeit()
        total = (end-start)*1000

        country = {'region': region,
                   'country': country_text,
                   'language': encode_text,
                   'time': total}

        final_countries.append(country)

    return final_countries


def encode_language(language):
    """
        Description
        ---------
        Encripta en formato SHA una cadena

        Parameters
        languaje: Cadena a encriptar
        
        Returns
        -------
        Text
            Cadena encriptada
    """
    return sha1(language.encode('utf-8')).hexdigest()


def create_df_and_calc(result):

    """
        Description
        ---------
        Crea un df a partir de una lista de diccionario y calcula el total, promedio, valor minimo y max 
        de todos los registros utilizando funciones de la libreria pandas 

        Parameters
        result: Lista de diccionario con los registros para el df
        
        Returns
        -------
        Float
            total: Sumatoria del total de tiempos
            mean: Promedio de todos los tiempos
            min: Valor más pequeño de todos los tiempos
            max: Valor más grande de todos los tiempos
    """

    df = pd.DataFrame(result)

    total = df["time"].sum()
    mean = df["time"].mean()
    min = df["time"].min()
    max = df["time"].max()

    return total, mean, min, max


def table_to_json(result):
    """
        Description
        ---------
        Genere un Json de la tabla creada y lo guarda como data.json
        
        Parameters
        ----------
        result: Valores de la tabla a convertir en .json
        
        Returns
        -------
        
    """
    with open('data.json', 'w') as file:
        json.dump(result, file)


#regions = get_regions()
#regions = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
#regions = ['Africa']

# for region in regions:
    # print(get_countries_by_region(region))

print(create_df_and_calc(get_all_countries()))

table_to_json(get_all_countries())
