#!/usr/bin/env python
'''
JSON ETL [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 2.0

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "2.0"

import json
import requests


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    print('# ---- Ejemplos con JSON Request ---- #')

    response = requests.get("https://jsonplaceholder.typicode.com/todos/1") # JSON único (el 1ero de la lista)
    # Se puede obtener el objeto JSON de dos formas distintas
    # El requests "crudo" solo trae el valor '200' (status_code) -> requests OK (reason)
    data = json.loads(response.text) # Para traer solo el texto (contenido)
    data = response.json() # Guardo en formato JSON
    print('Imprimir los datos traídos de la nube')
    print(json.dumps(data, indent=4))

    response = requests.get("https://jsonplaceholder.typicode.com/todos") # Toda la lista de JSONs
    data = response.json()

    for user in data:
        if user['userId'] > 2: # Filtra los JSON
            # No mostrar más de 2 usuarios
            # para no ocupar toda la pantalla con mensajes
            break
        print('El usuario {} completó {}? {}'.format(user['userId'],
                                                      user['title'],
                                                      user['completed']
                                                      ))

    print("terminamos")
