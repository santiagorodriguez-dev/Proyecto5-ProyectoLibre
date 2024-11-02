
import requests # type: ignore
import pandas as pd # type: ignore

def call_api_streaming(url, api_key, title):

    querystring = {"country":"ES","title":title,"show_type":"movie","output_language":"en"}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "streaming-availability.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()

def tratar_datos_streaming(datos):
   
    movies_data_streaming = []

    for d in datos:
       list_plataform = []
       for s in d['streamingOptions']['es']:            
            try:
                list_plataform.index(s['service']['name'])
            except ValueError:
                list_plataform.append(s['service']['name'])

       movies_data_streaming.append({
                "title": d['title'],
                "imdbId": d['imdbId'],
                "releaseYear": d['releaseYear'],
                "list_plataform": list_plataform
            })
       #nos quedamos con el primero que es el que nos interesa.
       break
   
    return pd.DataFrame(movies_data_streaming)

def get_data_streaming(url, api_key, title):

    datos = call_api_streaming(url, api_key, title)

    return tratar_datos_streaming(datos)

def tratar_datos_books(datos):
   
    books_data = []

    for d in datos:
       books_data.append({
                "title": d['name'],
                "rating": d['rating'],
                "releaseYear": d['year']
            })
       #nos quedamos con el primero que es el que nos interesa.
       break
   
    return pd.DataFrame(books_data)


def call_api_books(url, api_key, title):

    url = url + title;

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "hapi-books.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def get_data_books(url, api_key, title):

    datos = call_api_books(url, api_key, title)

    return tratar_datos_books(datos)


    
    