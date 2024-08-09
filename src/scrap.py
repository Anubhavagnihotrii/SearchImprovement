import requests
from bs4 import BeautifulSoup
import json

def scrape_trending_movies():
    url = "https://www.imdb.com/chart/moviemeter/"  # Example URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []

    for item in soup.select('td.titleColumn'):
        title = item.a.text
        year = item.span.text.strip('()')
        description = f"{title} ({year}) is a trending movie."  # Placeholder description

        movie = {
            "title": title,
            "release_year": year,
            "description": description
        }
        movies.append(movie)
    
    return movies

# Get trending movies data
trending_movies = scrape_trending_movies()

# Save data to JSON file
with open('trending_movies.json', 'w') as f:
    json.dump(trending_movies, f, indent=4)
