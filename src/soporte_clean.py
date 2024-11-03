import pandas as pd # type: ignore

def merge_dataframe(df_peliculas, df_books, df_streaming):

    df_peliculas['title'] = df_peliculas['title'].str.strip()
    df_books['title'] = df_books['title'].str.strip()
    df_streaming['title'] = df_streaming['title'].str.strip()

    df_merge = pd.merge(df_peliculas, df_books, how="left", on=["title"])
    df_all = pd.merge(df_merge, df_streaming, how="left", on=["title"])

    return df_all

def clean_data(df_all):

    df_all[['imdbId']] = df_all[['imdbId']].fillna(value='tt0000000')
    df_all[['list_plataform']] = df_all[['list_plataform']].fillna(value='')
    df_all[['releaseYear_y']] = df_all[['releaseYear_y']].fillna(value=0)
    df_all[['rating_y','releaseYear_x']] = df_all[['rating_y','releaseYear_y']].fillna(value=0)

    return df_all