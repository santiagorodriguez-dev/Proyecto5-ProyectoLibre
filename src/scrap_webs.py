from time import sleep
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
import pandas as pd # type: ignore
from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

def sacar_datos_imdb(url):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--lang=en")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    driver.implicitly_wait(5)

    movie_elements = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item")

    movies_data = []

    for movie in movie_elements:
        # si no hay datos, saltamos el registro
        try:
            title_element = movie.find_element(By.CLASS_NAME, "ipc-title__text")
            title = title_element.text.split(".")[1]

            year_element = movie.find_element(By.CLASS_NAME, "cli-title-metadata").find_elements(By.TAG_NAME, "span")[0]
            year = year_element.text

            duration_element = movie.find_element(By.CLASS_NAME, "cli-title-metadata").find_elements(By.TAG_NAME, "span")[1]
            duration = duration_element.text

            rating_element = movie.find_element(By.CLASS_NAME, "ipc-rating-star--rating")
            rating = rating_element.text

            votes_element = movie.find_element(By.CLASS_NAME, "ipc-rating-star--voteCount")
            votes = votes_element.text.strip("()").replace("(","")

            movies_data.append({
                "title": title,
                "year": year,
                "duration": duration,
                "rating": rating,
                "votes": votes
            })
        except:
            print("Error al capturar elemento sacar_datos_imdb()")

    driver.quit()

    return pd.DataFrame(movies_data)

def call_web(url):

    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Error en la llamada: {response.status_code}")


def sacar_datos_filmaffinity(url):

    html_content = call_web(url)

    soup = BeautifulSoup(html_content, 'html.parser')

    lista = soup.find_all('div', class_='full-card')

    movies = []

    for item in lista:
        # si no hay datos, saltamos el registro
        try:
            title = item.find('a', class_='d-none d-md-inline-block').get_text(strip=True)
            year = item.find('span', class_='mc-year ms-1').get_text(strip=True)
            rating = item.find('div', class_='avg mx-0').get_text(strip=True)
            
            movies.append({
                'title': title,
                'year': year,
                'rating': rating
            })
        except:
            print("Error al capturar sacar_datos_filmaffinity()")
    
    df = pd.DataFrame(movies)

    df = df.sort_values(by=['rating'], ascending=False)

    df = df.reset_index(drop=True)

    return df
    