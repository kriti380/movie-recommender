import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading dataset...")
movies = pd.read_csv("app/data/movies.csv")
movies = movies[["title", "genres"]]
movies.dropna(inplace=True)

print("Creating model folder...")
os.makedirs("app/model", exist_ok=True)

print("Vectorizing genres...")
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genres"])

print("Computing similarity matrix...")
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies["title"]).drop_duplicates()

print("Saving pickle files...")
pickle.dump(cosine_sim, open("app/model/similarity.pkl", "wb"))
pickle.dump(movies, open("app/model/movies.pkl", "wb"))
pickle.dump(indices, open("app/model/indices.pkl", "wb"))

print("Training completed successfully.")
