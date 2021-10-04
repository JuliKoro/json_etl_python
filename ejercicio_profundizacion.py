import requests
import json
import matplotlib as plt

url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquileres%20Mendoza%20&limit=50'

def fetch():
    pass


def transform(dataset, min, max):
    pass


def report(data):
    pass


if __name__ == "_main_":
    min = 0
    max = 1

    dataset = fetch()
    data = transform(dataset, min, max)
    report(data)