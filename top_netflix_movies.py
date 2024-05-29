import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.digitaltrends.com/movies/best-movies-on-netflix"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

movies = bs.select("h3")
crew = bs.select("div.b-media__value")
genre = bs.select("div.b-media__value")

list_of_movies = [a.get_text(strip=True) for a in movies]
list_of_crew = [b.get_text(strip=True) for b in crew][1::3]
list_of_genre = [c.get_text(strip=True) for c in genre][0::3]

list = []
for index in range(0,len(list_of_movies)):
    data = {"movie name":list_of_movies[index],"crew":list_of_crew[index],"genre":list_of_genre[index]}

    list.append(data)


df = pd.DataFrame(list)
df.to_csv('top_netflix_movies.csv', index=False)
df.to_excel("top 50 netflix movies.xlsx", index=False)
print(list)
