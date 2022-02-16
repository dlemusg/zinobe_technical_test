import pandas as pd
import requests
import timeit
from hashlib import sha1
import json


def get_coutries_by_region(regions):

    final_countries = []

    for region in regions:
        try:
            countries = requests.get(
                f'https://restcountries.com/v3.1/region/{region}').json()

            final_countries += final_countrie_list(countries)           

        except:
            next

    return final_countries


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

    

    return final_countrie_list(countries)


def final_countrie_list(countries):

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