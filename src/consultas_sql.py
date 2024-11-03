

import pandas as pd # type: ignore
"""
Nos traemos los datos de las tablas, para poder analizar en dataframe

"""

def select_data(conn, cursor, id):
    try:

        query = f"""
        SELECT 
            webs.id,
            webs.nombre,
            peliculas.*
        FROM webs
        LEFT JOIN peliculas ON webs.id = peliculas.id_web
        WHERE webs.id = {id};
        """
        cursor.execute(query)

        columnas = []

        for c in cursor.description:
            columnas.append(c[0])

        resultados = cursor.fetchall()

        df = pd.DataFrame(resultados,columns=columnas)

        return df
        
    except:
        print(f"Error en select_data(conn, cursor, id):")
    finally:
        if cursor:
            cursor.close()
        if conn:
           conn.close()