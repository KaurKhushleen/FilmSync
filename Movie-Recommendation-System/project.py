import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{str(movie_id)}?api_key=7c08485ee94bda73964423a1eb7c97df&language=en-US"
    response = (requests.get(url)).json()
    path = "https://image.tmdb.org/t/p/w500/" + response["poster_path"]
    return path

def recommend(movie):
    movie_index = movies_df[movies_df["title"] == movie].index[0]
    distances = similarities[movie_index]
    recommendations_object = sorted(list(enumerate(distances)), reverse = True, key = lambda x : x[1])[1:6]
    recommendations_names = []
    recommendations_posters = []

    for recommendation in recommendations_object:
        recommendation_index = recommendation[0]
        recommendations_names.append(movies_df.iloc[recommendation_index].title)
        recommendations_posters.append(fetch_poster(movies_df.iloc[recommendation_index].movie_id))

    return recommendations_names, recommendations_posters

def make_columns(num, names, posters):
    cols = st.columns(num)
    for i in range(num):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])



st.title("Film-Sync🎥🍿")

movies_df = pickle.load(open("movies.pkl", "rb"))
similarities = pickle.load(open("similarity.pkl", "rb"))

movies_list = movies_df["title"].values
#options = st.selectbox("Movie", movies_list)
movie_input = st.selectbox("Movie", movies_list)

if st.button("Recommend", icon = "🎬", use_container_width = True):
    names, posters = recommend(movie_input)
    make_columns(5, names, posters)