import requests,json,os
from dotenv import load_dotenv
load_dotenv()

def getPopularMovies():
    url = "https://api.themoviedb.org/3/movie/popular"
    headers = {
    "accept": "application/json",
    "Authorization": os.getenv("BEARER_TOKEN")
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    with open("data\\getPopularMovies.json", "a", encoding="utf-8") as f:
        json.dump(data,f, ensure_ascii=False, indent=4)
    f.close()

def getTopRatedMovies():
    url= "https://api.themoviedb.org/3/movie/top_rated"
    headers = {
    "accept": "application/json",
    "Authorization": os.getenv("BEARER_TOKEN")
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    with open("data\\getTopRatedMovies.json", "a", encoding="utf-8") as f:
        json.dump(data,f, ensure_ascii=False, indent=4)
    f.close()

def getMovieRecommendations():
    url = "https://api.themoviedb.org/3/movie/573435/recommendations"
    headers = {
    "accept": "application/json",
    "Authorization": os.getenv("BEARER_TOKEN")
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    with open("data\\getMovieRecommendations.json", "a", encoding="utf-8") as f:
        json.dump(data,f, ensure_ascii=False, indent=4)
    f.close()


getPopularMovies()
getTopRatedMovies()
getMovieRecommendations()