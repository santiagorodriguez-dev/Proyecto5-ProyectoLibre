import pandas as pd # type: ignore

def merge_dataframe(df_peliculas_imdb, df_books_imdb, df_streaming_imdb):

    df_peliculas_imdb['title'] = df_peliculas_imdb['title'].str.strip()
    df_books_imdb['title'] = df_books_imdb['title'].str.strip()
    df_streaming_imdb['title'] = df_streaming_imdb['title'].str.strip()

    df_merge = pd.merge(df_peliculas_imdb, df_books_imdb, how="left", on=["title"])
    df_all = pd.merge(df_merge, df_streaming_imdb, how="left", on=["title"])

    return df_all

def clean_data(df_all):

    df_all[['imdbId']] = df_all[['imdbId']].fillna(value='tt0000000')
    df_all[['list_plataform']] = df_all[['list_plataform']].fillna(value='')
    df_all[['releaseYear_y']] = df_all[['releaseYear_y']].fillna(value=0)

    return df_all