import json
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import XSD

# Load JSON data
with open('data\\getTopRatedMovies.json', 'r') as f:
    data = json.load(f)

# Define namespaces
EX = Namespace("http://example.com/schema#")
# Create a new graph
g = Graph()

# Function to create RDF triples from JSON
def create_movie_rdf(movie):
    movie_uri = EX[f"movie_{movie['id']}"]
    g.add((movie_uri, RDF.type, EX.Movie))
    g.add((movie_uri, EX.title, Literal(movie['title'])))
    g.add((movie_uri, EX.original_title, Literal(movie['original_title'])))
    g.add((movie_uri, EX.overview, Literal(movie['overview'])))
    g.add((movie_uri, EX.media_type, Literal(movie['media_type'])))
    g.add((movie_uri, EX.adult, Literal(movie['adult'], datatype=XSD.boolean)))
    g.add((movie_uri, EX.original_language, Literal(movie['original_language'])))
    g.add((movie_uri, EX.popularity, Literal(movie['popularity'], datatype=XSD.float)))
    g.add((movie_uri, EX.release_date, Literal(movie['release_date'], datatype=XSD.date)))
    
    # Add genre IDs
    for genre_id in movie['genre_ids']:
        g.add((movie_uri, EX.genre_id, Literal(genre_id)))

# Process each movie
for movie in data['results']:
    create_movie_rdf(movie)

# Serialize the graph to Turtle format
ttl_data = g.serialize(format='turtle')

# Save to a file
with open('movies.ttl', 'w') as f:
    f.write(ttl_data)
