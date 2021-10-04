# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado

    json_data = {
        "nombre": "Julián",
        "apellido": "Koroluk",
        "DNI": 42315678,
        "vestimenta": [
            {
                "prenda": "zapatillas",
                "cantidad": 2,
            },
            {
               "prenda": "remera",
                "cantidad": 3, 
            },
            {
                "prenda": "jeans",
                "cantidad": 1,
            },
            {
                "prenda": "buzo",
                "cantidad": 2,
            }
        ]
    }
    with open('armario.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)


def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior

    with open('armario.json', 'r') as jsonfile:
        json_data_ld = json.load(jsonfile)
    json_string = json.dumps(json_data_ld, indent=4)
    print('Armario:\n', json_string)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    serializar()
    deserializar()

    print("terminamos")