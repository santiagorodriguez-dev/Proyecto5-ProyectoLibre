import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore


def visualizar_comparativa_rating(df, web):
    """
    Visualiza un gráfico de dispersión que compara el rating de video y el rating de libro
    para cada película, diferenciando por el título.

    Args:
        df (DataFrame): DataFrame que contiene información sobre películas, incluyendo
                        rating de video y rating de libro.
        web (str): Nombre de la fuente de datos para incluir en el título del gráfico.
    """
    plt.figure(figsize=(18, 6))
    sns.scatterplot(data=df, x="rating_video", y="rating_libro", hue="title", s=100)

    plt.xlabel("Rating de Video (0-10)")
    plt.ylabel("Rating de Libro (0-5)")
    plt.title(f"Comparación de Rating Video vs Rating Libro por Película en: {web} ")

    plt.legend(title="", bbox_to_anchor=(0.5, -0.2), loc='upper center', ncol=4)
    plt.grid(True)
    plt.show()


def visualizar_comparativa_plataformas(df, web):
    """
    Visualiza un gráfico de barras que muestra la mediana del rating de video en relación
    con el número de plataformas de streaming.

    Args:
        df (DataFrame): DataFrame que contiene información sobre el número de plataformas
                        y rating de video.
        web (str): Nombre de la fuente de datos para incluir en el título del gráfico.
    """
    mean_ratings = df.groupby('numero_plataformas')['rating_video'].median().reset_index()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=mean_ratings, x='numero_plataformas', y='rating_video')

    plt.xlabel("Número de Plataformas")
    plt.ylabel("Mediana Rating de Video")
    plt.title(f"Relación entre Número de Plataformas y la Mediana Rating de Video en: {web}")
    plt.xticks(rotation=0)

    plt.show()


def visualizar_cantidad(df, web):
    """
    Visualiza un gráfico de barras que muestra el número de películas junto con las medianas
    del rating de video y libro, agrupados por el número de plataformas.

    Args:
        df (DataFrame): DataFrame que contiene información sobre películas, incluyendo
                        el número de plataformas y sus ratings.
        web (str): Nombre de la fuente de datos para incluir en el título del gráfico.
    """
    grouped_data = df.groupby('numero_plataformas').agg(
        num_peliculas=('title', 'count'),
        mediana_rating_video=('rating_video', 'median'),
        mediana_rating_libro=('rating_libro', 'median')
    ).reset_index()

    fig, ax1 = plt.subplots(figsize=(10, 6))

    sns.barplot(data=grouped_data, x='numero_plataformas', y='num_peliculas', color='skyblue', ax=ax1)
    ax1.set_ylabel("Número de Películas", color='skyblue')
    ax1.set_xlabel("Número de Plataformas")

    ax2 = ax1.twinx()
    sns.lineplot(data=grouped_data, x='numero_plataformas', y='mediana_rating_video', marker='o', color='orange', label='Mediana Rating Video', ax=ax2)
    sns.lineplot(data=grouped_data, x='numero_plataformas', y='mediana_rating_libro', marker='o', color='green', label='Mediana Rating Libro', ax=ax2)
    ax2.set_ylabel("Mediana de Ratings")

    ax2.legend(loc="upper left")
    plt.title(f"Número de Películas y Mediana de Ratings por Número de Plataformas en {web}")
    plt.show()
