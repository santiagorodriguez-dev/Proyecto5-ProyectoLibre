import pandas as pd  # type: ignore

def merge_dataframe(df_peliculas, df_books, df_streaming):
    """
    Combina tres DataFrames en uno solo utilizando la columna 'title' como clave de unión.

    Args:
        df_peliculas (DataFrame): DataFrame que contiene información sobre películas.
        df_books (DataFrame): DataFrame que contiene información sobre libros.
        df_streaming (DataFrame): DataFrame que contiene información sobre plataformas de streaming.

    Returns:
        DataFrame: Un DataFrame que combina la información de las películas, libros y plataformas de streaming.
    """
    df_peliculas['title'] = df_peliculas['title'].str.strip()
    df_books['title'] = df_books['title'].str.strip()
    df_streaming['title'] = df_streaming['title'].str.strip()

    df_merge = pd.merge(df_peliculas, df_books, how="left", on=["title"])
    df_all = pd.merge(df_merge, df_streaming, how="left", on=["title"])

    return df_all

def clean_data(df_all):
    """
    Limpia y prepara el DataFrame combinado reemplazando valores nulos por valores predeterminados.

    Args:
        df_all (DataFrame): DataFrame combinado que contiene información de películas, libros y plataformas de streaming.

    Returns:
        DataFrame: Un DataFrame limpio con valores nulos reemplazados por valores predeterminados.
    """
    df_all[['imdbId']] = df_all[['imdbId']].fillna(value='tt0000000')
    df_all[['list_plataform']] = df_all[['list_plataform']].fillna(value='')
    df_all[['releaseYear_y']] = df_all[['releaseYear_y']].fillna(value=0)
    df_all[['rating_y', 'releaseYear_x']] = df_all[['rating_y', 'releaseYear_y']].fillna(value=0)

    return df_all
