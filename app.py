from turtle import pd
import pandas as pd
import requests


def get_regions():
    return 0

def get_countries_by_region(region):
    countries = requests.get(f'https://restcountries.com/v3.1/region/{region}').json()

    final_countries = []

    for country in countries:
        country = {'region': region, 
                    'country': country['name']['official'], 
                    'languaje': list(country['languages'].values())[0]}
        final_countries.append(country)

    
    return final_countries







#regions = get_regions()
#regions = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
regions = ['Africa']

for region in regions:
    print(get_countries_by_region(region))

