import requests  # type: ignore
import pandas as pd  # type: ignore

def call_api_streaming(url, api_key, title):
    """
    Llama a la API de Streaming para obtener información sobre una película específica.

    Args:
        url (str): La URL de la API de Streaming.
        api_key (str): La clave de API necesaria para autenticar la solicitud.
        title (str): El título de la película que se desea buscar.

    Returns:
        dict: Un diccionario con la respuesta JSON de la API que contiene información sobre la película.
    """
    querystring = {"country": "ES", "title": title, "show_type": "movie", "output_language": "en"}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "streaming-availability.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()

def tratar_datos_streaming(datos):
    """
    Procesa los datos obtenidos de la API de Streaming para extraer información relevante de las películas.

    Args:
        datos (list): Lista de diccionarios que contienen información sobre las películas obtenida de la API.

    Returns:
        DataFrame: Un DataFrame de pandas que contiene el título, el ID de IMDb, el año de lanzamiento y las plataformas de streaming de las películas.
    """
    movies_data_streaming = []

    for d in datos:
        try:
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
            # nos quedamos con el primero que es el que nos interesa.
            break
        except:
            pass

    return pd.DataFrame(movies_data_streaming)

def get_data_streaming(url, api_key, df):
    """
    Obtiene datos de streaming para una lista de películas.

    Args:
        url (str): La URL de la API de Streaming.
        api_key (str): La clave de API necesaria para autenticar la solicitud.
        df (DataFrame): Un DataFrame de pandas que contiene una lista de películas (títulos).

    Returns:
        DataFrame: Un DataFrame de pandas que contiene información de streaming de todas las películas procesadas.
    """
    df_final = pd.DataFrame()

    for index, row in df.iterrows():
        datos = call_api_streaming(url, api_key, row['title'])
        df_temp = tratar_datos_streaming(datos)
        df_final = pd.concat([df_final, df_temp])

    df_final = df_final.reset_index(drop=True)

    return df_final

def tratar_datos_books(datos, title):
    """
    Procesa los datos obtenidos de la API de libros para extraer información relevante sobre un libro específico.

    Args:
        datos (list): Lista de diccionarios que contienen información sobre los libros obtenida de la API.
        title (str): El título del libro para el que se están procesando los datos.

    Returns:
        DataFrame: Un DataFrame de pandas que contiene el título, el rating y el año de publicación del libro.
    """
    books_data = []

    for d in datos:
        try:
            books_data.append({
                "title": title,
                "rating": d['rating'],
                "releaseYear": d['publishedYear']
            })
            # nos quedamos con el primero que es el que nos interesa.
            break
        except:
            pass

    return pd.DataFrame(books_data)

def call_api_books(url, api_key, title):
    """
    Llama a la API de Goodreads para obtener información sobre un libro específico.

    Args:
        url (str): La URL de la API de Goodreads.
        api_key (str): La clave de API necesaria para autenticar la solicitud.
        title (str): El título del libro que se desea buscar.

    Returns:
        dict: Un diccionario con la respuesta JSON de la API que contiene información sobre el libro.
    """
    querystring = {"keyword": title}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "goodreads12.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()

def get_data_books(url, api_key, df):
    """
    Obtiene datos de libros para una lista de títulos.

    Args:
        url (str): La URL de la API de Goodreads.
        api_key (str): La clave de API necesaria para autenticar la solicitud.
        df (DataFrame): Un DataFrame de pandas que contiene una lista de libros (títulos).

    Returns:
        DataFrame: Un DataFrame de pandas que contiene información de libros procesados.
    """
    df_final = pd.DataFrame()

    for index, row in df.iterrows():
        datos = call_api_books(url, api_key, row['title'])
        df_temp = tratar_datos_books(datos, row['title'])

        if (df_temp.shape[0] > 0):
            df_final = pd.concat([df_final, df_temp])

    df_final = df_final.reset_index(drop=True)

    return df_final
