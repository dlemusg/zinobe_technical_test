"""
OK ::: De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
OK ::: En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
OK ::: La tabla debe ser creada en un DataFrame con la libreria PANDAS
OK ::: Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
OK ::: Guarde el resultado en sqlite.
OK ::: Genere un Json de la tabla creada y guardelo como data.json
OK ::: La prueba debe ser entregada en un repositorio git.
"""

from core_app import get_coutries_by_region, get_all_countries, create_df_and_calc, table_to_json
from database import insert_row, sql_fetch


if __name__ == "__main__":

    print("1. Obteniendo data de los paises")
    #regions = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    #result = get_coutries_by_region(regions)
    result = get_all_countries()
    print("2. Calculando total, median, min, max a partir del df")
    total, median, min, max = create_df_and_calc(result)
    print(f'\tTotal: {total}')
    print(f'\tPromedio: {median}')
    print(f'\tMinimo: {min}')
    print(f'\tMaximo: {max}' )
    print("3. Insertando datos sobre la bd")
    insert_row(result)
    print("4. Generando data.json ")
    table_to_json(result)
    print("5. Comprobar bd")
    print(sql_fetch())
    