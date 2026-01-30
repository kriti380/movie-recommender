import streamlit as st
import pickle
import pandas as pd

with open("model/movies.pkl", "rb") as f:
    movies = pickle.load(f)
with open("model/indices.pkl", "rb") as f:
    indices = pickle.load(f)
with open("model/similarity.pkl", "rb") as f:
    cosine_sim = pickle.load(f)

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommender")
st.write("Select a movie to get similar recommendations.")

movie_name = st.selectbox("Choose a movie:", movies['title'].tolist())

def recommend(movie_title, top_n=6):
    matches = movies[movies['title'] == movie_title]
    if matches.empty:
        return []
    idx = indices[movie_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [s for s in sim_scores if s[0] != idx][:top_n]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

if st.button("Recommend"):
    recommendations = recommend(movie_name)
    if recommendations:
        st.subheader("You may also like:")
        cols = st.columns(3)  
        for i, rec in enumerate(recommendations):
            with cols[i % 3]:
                st.write(f"🎬 {rec}")
    else:
        st.warning("No recommendations found.")
