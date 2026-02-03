import streamlit as st
import pickle

# Load trained data
cosine_sim = pickle.load(open("app/model/similarity.pkl", "rb"))
movies = pickle.load(open("app/model/movies.pkl", "rb"))
indices = pickle.load(open("app/model/indices.pkl", "rb"))

def recommend(movie_title, top_n=6):
    if movie_title not in indices:
        return []
    idx = indices[movie_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [s for s in sim_scores if s[0] != idx][:top_n]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()


st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title("🎬 Movie Recommendation System")

movie_name = st.selectbox("Choose a movie:", movies['title'].tolist())

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
