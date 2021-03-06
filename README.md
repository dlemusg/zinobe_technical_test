# zinobe_technical_test
zinobe's technical test

## Problema

|  Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  Africa | Angola  |  AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms  |


Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

- De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
- En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
- La tabla debe ser creada en un DataFrame con la libreria PANDAS
- Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
- Guarde el resultado en sqlite.
- Genere un Json de la tabla creada y guardelo como data.json
- La prueba debe ser entregada en un repositorio git.



**Es un plus si:**
* No usa famework
* Entrega Test Unitarios
* Presenta un dise帽o de su solucion.


## Dise帽o de la soluci贸n

### Propuesta de implementaci贸n
![Image_text](https://github.com/dlemusg/zinobe_technical_test/blob/main/images/class_zinobe.jpeg)

### Pre-requisitos 馃搵
Para el correcto funcionamiento del proyecto se deben instalar las siguientes librerias como prerequisitos
```
pip install -r requirements.txt
```

### Ejecutando las pruebas 鈿欙笍
Para la ejecuci贸n de las pruebas dentro de la carpeta del proyecto ejecutar el siguiente comando:
```
python -m unittest test_base.py
```
#### Resultado esperado
![Image_text](https://github.com/dlemusg/zinobe_technical_test/blob/main/images/out_test_base.jpg)


### Ejecuci贸n 馃摝
Para la ejecuci贸n del programa, dentro de la carpeta del proyecto ejecutar el siguiente comando:
```
python app.py
```
#### Resultado esperado
![Image_text](https://github.com/dlemusg/zinobe_technical_test/blob/main/images/out_app.jpg)

### Construido con 馃洜锔?
* **Pandas:** Libreria utilizada para la creaci贸n del dataframe y el calculo del total, media, min y max
* **requests:** Libreria utilizada para hacer las solicitudes a la api y obtener los datos
* **sqlite3:** Libreria utilizada para crear el motor de base de datos. 
* **unittest:** Libreria utilizada para la construcci贸n de pruebas unitarias


### Autores 鉁掞笍


* **David Lemus**