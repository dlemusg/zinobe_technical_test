"""
OK ::: De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
OK ::: En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
OK ::: La tabla debe ser creada en un DataFrame con la libreria PANDAS
OK ::: Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
Guarde el resultado en sqlite.
OK ::: Genere un Json de la tabla creada y guardelo como data.json
La prueba debe ser entregada en un repositorio git.
"""

from core_app import get_coutries_by_region, get_all_countries, create_df_and_calc, table_to_json


if __name__ == "__main__":

    print(create_df_and_calc(get_all_countries()))


# regions = get_regions()
# regions = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
# regions = ['Africa']

# for region in regions:
    # print(get_countries_by_region(region))

#print(create_df_and_calc(get_all_countries()))

#print(create_df_and_calc(get_coutries_by_region(['africa'])))
#print(get_coutries_by_region(['Africa']))

#table_to_json(get_all_countries())
