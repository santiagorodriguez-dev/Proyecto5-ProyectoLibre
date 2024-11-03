# Análisis comparativo de Rating de peliculas basadas en libros

## Fuentes

**www.imdb.com**

<div style="text-align: center;">
  <img src="https://github.com/santiagorodriguez-dev/Proyecto5-ProyectoLibre/blob/main/imagenes/01.PNG" alt="esquema" />
</div>

**www.filmaffinity.com**

<div style="text-align: center;">
  <img src="https://github.com/santiagorodriguez-dev/Proyecto5-ProyectoLibre/blob/main/imagenes/02.PNG" alt="esquema" />
</div>

## Fases

**Scraping de datos**: Extraer información de la web de www.filmaffinity.com y www.imdb.com para cada uno de los top de peliculas.

**Datos de apis**: Se ha extraido la informacion de libros de https://rapidapi.com/UnitedAPI/api/goodreads12

**Datos de apis**: Se ha extraido la informacion de peliculas en plataformas de https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability

**Almacenamiento en base de datos**: se crea una base de datos en SQL que almacene la información recolectada de manera estructurada.

**Estructura de BD**: Se han creado dos tablas con los datos de peliculas y webs.
<div style="text-align: center;">
  <img src="https://github.com/santiagorodriguez-dev/Proyecto5-ProyectoLibre/blob/main/imagenes/03.PNG" alt="esquema" />
</div>

### Analisis de datos: Graficos sobre diferentes comparaciones de ratings.

#### Este gráfico es útil para observar la relación entre los ratings de video y libro para cada película en la plataforma filmaffinity y facilita la detección de patrones o tendencias, como si existen películas que tienen ratings altos o bajos, o si hay discrepancias entre los ratings de video y libro.

<div style="text-align: center;">
  <img src="https://github.com/santiagorodriguez-dev/Proyecto5-ProyectoLibre/blob/main/imagenes/04.png" alt="esquema" />
</div>

#### Este gráfico es útil para observar la relación entre los ratings de video y libro para cada película en la plataforma imdb y facilita la detección de patrones o tendencias, como si existen películas que tienen ratings altos o bajos, o si hay discrepancias entre los ratings de video y libro.

<div style="text-align: center;">
  <img src="https://github.com/santiagorodriguez-dev/Proyecto5-ProyectoLibre/blob/main/imagenes/05.png" alt="esquema" />
</div>

#### Este gráfico  muestra la relación entre el número de plataformas en las que están disponibles las películas, el número total de películas por ese número de plataformas y las medianas de los ratings de video y libro sobre la web filmaffinity

<div style="text-align: center;">
  <img src="https://github.com/santiagorodriguez-dev/Proyecto5-ProyectoLibre/blob/main/imagenes/06.png" alt="esquema" />
</div>

#### Este gráfico  muestra la relación entre el número de plataformas en las que están disponibles las películas, el número total de películas por ese número de plataformas y las medianas de los ratings de video y libro sobre la web imdb

<div style="text-align: center;">
  <img src="https://github.com/santiagorodriguez-dev/Proyecto5-ProyectoLibre/blob/main/imagenes/07.png" alt="esquema" />
</div>

## Conclusiones Finales:
   - Con los datos analizados, observamos patrones que basicamente demuestran que en la mayoria de ocasiones el libro es mejor que la pelicula.

#### Propuestas de Mejora:
   - Realizar la descarga de datos a lo largo de diferentes fechas, para observar si cambia el patron a lo largo del tiemnpo.
  
## Construido con 🛠️

* [Pyhton](https://www.python.org/) - Lenguaje utilizado
* [Numpy](https://numpy.org/doc/stable/) - Numpy
* [seaborn](https://seaborn.pydata.org/tutorial.html) - Seaborn
* [matplotlib](https://matplotlib.org/stable/users/index) - matplotlib
* [pandas](https://pandas.pydata.org/docs/) - pandas
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - BeautifulSoup
* [selenium](https://www.selenium.dev/documentation/) - selenium
* [Visual Studio Code](https://code.visualstudio.com/) - IDE desarrollo
  
## Autores ✒️

* **Santiago Rodriguez** - [santiagorodriguez-dev](https://github.com/santiagorodriguez-dev)
