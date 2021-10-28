import requests
import json
import matplotlib.pyplot as plt
import matplotlib.axes


def fetch(ciudad):
    '''
    Consumo de datos
    
    Consume los datos de la 'url' y los filtra según su "__"currency_id"__".
    Retorna 'dataset' que es una lista de diccionarios.

    dataset = [{"price": ..., "condition": ..., "area": ...}, ...]
    '''
    if ' ' in ciudad:
        ciudad = ciudad.replace(' ', '%20')
    
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquileres%20'+ciudad+'%20&limit=50'
    response = requests.get(url)
    data = response.json()
    dataset = [{'price': item["price"], 'condition': item["condition"], 'area': item["attributes"][1]["value_struct"]} for item in data["results"] if item["currency_id"] == "ARS"] # Filtra el json
    return dataset


def transform(dataset, min, max):
    '''
    Transformación de la información

    Filtra y divide el 'dataset' en tres listas distintas, separandolas según su 'price'.
    Retorna 1 lista con el tamaño de cada una de las listas filtradas:
    min_count: Cantidad de elementos con 'price' < 'min'
    min_max_count: Cantidad de elementos con min < 'price' < 'max'
    max_count: Cantidad de elementos con 'price' > 'max'
    precios: Precios de todos los departamentos
    areas: Áreas de todos los departamentos en m2

    @param List dataset Diccionarios con el 'price', 'condition', y 'area' de c/ elemento
    @param Float min Precio mínimo del rango
    @param Float max Precio máximo del rango
    '''
    min_price = [x for x in dataset if x['price'] < min]
    min_max_price = [x for x in dataset if min < x['price'] < max]
    max_price = [x for x in dataset if x['price'] > max]
    precios = [x['price'] for x in dataset if x['area'] != None]
    dict_areas = [x['area'] for x in dataset]
    areas = [x['number'] for x in dict_areas if x != None]

    min_count = len(min_price)
    min_max_count = len(min_max_price)
    max_count = len(max_price)

    return [min_count, min_max_count, max_count, precios, areas]


def report(data, min, max):
    '''
    Reporte
    
    Realiza los gráficos en base a los datos obtenidos: 
    - Uno de torta que nos de la idea de como se reparten los precios de los alquileres según 
    los parámetros "min" y "max".
    - Otro tipo Scatterplot, que refleja la relación entre los precios y la superfice de los
    departamentos.

    @param List data Cantidades de elementos según los rangos de precios
    @param Float min Precio mínimo del rango
    @param Float max Precio máximo del rango
    '''
    data1 = data[0:3]
    precios = data[3]
    areas = data[4]
    
    fig = plt.figure()
    fig.suptitle('Departamentos según precio', fontsize=16)
    ax = fig.add_subplot()

    etiquetas = ['< $'+str(min), '$'+str(min)+'-'+'$'+str(max), '> $'+str(max)]

    ax.pie(data1, labels=etiquetas, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    plt.show()

    fig2 = plt.figure()
    fig2.suptitle('Precios vs Área', fontsize=16)
    ax2 = fig2.add_subplot()
    ax2.set_xlabel('Precio de alquiler [$ARS]')
    ax2.set_ylabel('Superficie habitable [m2]')
    ax2.scatter(precios, areas, c='darkcyan', label='Departamentos')
    ax2.legend()
    ax2.set_facecolor('whitesmoke')
    ax2.grid('solid')
    plt.show()


if __name__ == '__main__':
    print('¡Bienvenido al Buscador de Alquiler de Departamentos!\nPowered by MELI')
    ciudad = input('Ingrese la ciudad que desea buscar: ')
    min = float(input('Ingrese precio mínimo: $'))
    max = float(input('Ingrese precio máximo: $'))

    dataset = fetch(ciudad)
    data = transform(dataset, min, max)
    report(data, min, max)