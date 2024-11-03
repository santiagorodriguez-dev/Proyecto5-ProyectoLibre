
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
            #nos quedamos con el primero que es el que nos interesa.
            break
       except:
           pass
   
    return pd.DataFrame(movies_data_streaming)

def get_data_streaming(url, api_key, df):
    df_final = pd.DataFrame()

    for index, row in df.iterrows():
        datos = call_api_streaming(url, api_key, row['title'])
        df_temp = tratar_datos_streaming(datos)
        df_final = pd.concat([df_final,df_temp])

    df_final = df_final.reset_index(drop=True)

    return df_final

def tratar_datos_books(datos, title):
   
    books_data = []

    for d in datos:
        try:
            books_data.append({
                        "title": title,
                        "rating": d['rating'],
                        "releaseYear": d['publishedYear']
                    })
            #nos quedamos con el primero que es el que nos interesa.
            break
        except:
            pass
   
    return pd.DataFrame(books_data)


def call_api_books(url, api_key, title):

    querystring = {"keyword":title}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "goodreads12.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()

def get_data_books(url, api_key, df):

    df_final = pd.DataFrame()

    for index, row in df.iterrows():
        datos = call_api_books(url, api_key, row['title'])
        df_temp = tratar_datos_books(datos, row['title'])

        if (df_temp.shape[0] > 0):
            df_final = pd.concat([df_final,df_temp])

    df_final = df_final.reset_index(drop=True)

    return df_final



    
    