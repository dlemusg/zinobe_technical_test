"""
De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
La tabla debe ser creada en un DataFrame con la libreria PANDAS
Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
Guarde el resultado en sqlite.
Genere un Json de la tabla creada y guardelo como data.json
La prueba debe ser entregada en un repositorio git.
"""


from turtle import pd
import pandas as pd
import requests
from hashlib import sha1


def get_regions():
    return 0

def get_countries_by_region(region):
    countries = requests.get(f'https://restcountries.com/v3.1/region/{region}').json()

    final_countries = []

    for country in countries:
        country = {'region': region, 
                    'country': country['name']['official'], 
                    'languaje': encode_language(list(country['languages'].values())[0])}
        final_countries.append(country)

    return final_countries
    
def encode_language(language):
    return sha1(language.encode('utf-8')).hexdigest()
    
    

#regions = get_regions()
#regions = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
regions = ['Africa']

for region in regions:
    print(get_countries_by_region(region))

