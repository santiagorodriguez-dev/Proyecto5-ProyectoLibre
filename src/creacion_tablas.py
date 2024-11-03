

import pandas as pd # type: ignore

webs_dicc = {'filmaffinity': 1, 'imdb': 2}

def create_table_webs(conn, cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS webs (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(50) UNIQUE NOT NULL
            )
        """)
        conn.commit()
        print("Tabla 'webs' creada con éxito.")
    except:
        print(f"Error al crear la tabla: webs")
    
def insert_webs(conn, cursor):
    """
    Inserta las webs del diccionario en la tabla 'webs'.
    """
    try:
        for nombre, id in webs_dicc.items():
            cursor.execute("""
                INSERT INTO webs (id, nombre) VALUES (%s, %s)
                ON CONFLICT (nombre) DO NOTHING
            """, (id, nombre))
        conn.commit()
        print("webs insertadas con éxito.")
    except Exception as e:
        print(f"Error al insertar las webs: {e}")


def create_table_peliculas(conn, cursor):
    try:
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS peliculas (
                id SERIAL PRIMARY KEY,
                title VARCHAR(300) NOT NULL,
                rating_video DECIMAL(2, 1),
                rating_libro VARCHAR(100),
                numero_plataformas INTEGER,
                id_web INTEGER NOT NULL,
                FOREIGN KEY (id_web) REFERENCES webs (id)
            )
        """)
        conn.commit()
        print("Tabla 'peliculas' creada con éxito.")
    except:
        print(f"Error al crear la tabla 'peliculas")


def insert_data_peliculas(conn, cursor, df):
    """
    Carga un DataFrame en la tabla 'peliculas'.
    """
    try:
        for index, row in df.iterrows():
                numero_plataformas_calc = 0
                try:
                     result = row['list_plataform'].split(",")
                     contador = 0
                     for i in result:
                         contador = contador + 1

                     numero_plataformas_calc = contador
                except:
                    pass

                cursor.execute("""
                    INSERT INTO peliculas (title, rating_video, rating_libro, id_web, numero_plataformas)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    row['title'],
                    float(row['rating_x']),
                    row['rating_y'],
                    row['id_web'],
                    numero_plataformas_calc
                ))
                conn.commit()
        print("Datos cargados con éxito en la tabla 'peliculas'.")
    except :
        print(f"Error al cargar datos en la tabla: peliculas")


def main(conn, cursor, df):
    create_table_webs(conn,cursor)

    insert_webs(conn,cursor)

    create_table_peliculas(conn,cursor)

    insert_data_peliculas(conn,cursor,df)

    

