import pickle
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load dataset
movies = pd.read_csv("data/movies.csv")
movies = movies[["title", "genres"]]
movies.dropna(inplace=True)

print("Dataset shape:", movies.shape)
print(movies.head())

# Create model folder if missing
if not os.path.exists("model"):
    os.mkdir("model")

# Check if model exists, else train and save
if os.path.exists("model/similarity.pkl") and os.path.exists("model/movies.pkl") and os.path.exists("model/indices.pkl"):
    with open("model/similarity.pkl", "rb") as f:
        cosine_sim = pickle.load(f)
    with open("model/movies.pkl", "rb") as f:
        movies = pickle.load(f)
    with open("model/indices.pkl", "rb") as f:
        indices = pickle.load(f)
    print("Loaded saved model.")
else:
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

    # Save model with pickle
    with open("model/similarity.pkl", "wb") as f:
        pickle.dump(cosine_sim, f)
    with open("model/movies.pkl", "wb") as f:
        pickle.dump(movies, f)
    with open("model/indices.pkl", "wb") as f:
        pickle.dump(indices, f)

    print("Model trained and saved.")

# Recommendation function
def recommend(movie_title, top_n=5):
    matches = movies[movies['title'].str.lower().str.contains(movie_title.lower(), regex=False)]

    if matches.empty:
        print("Movie not found in the dataset.")
        return []

    matched_title = matches['title'].iloc[0]
    idx = indices[matched_title]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [s for s in sim_scores if s[0] != idx]
    sim_scores = sim_scores[:top_n]
    
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

# CLI entry
if __name__ == "__main__":
    movie_name = input("Enter a movie you like: ")
    recommendations = recommend(movie_name)

    print("\nBecause you liked:", movie_name)
    print("You may also like:")
    for rec in recommendations:
        print("✨", rec)
