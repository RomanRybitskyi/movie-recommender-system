import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), key=lambda x:x[1], reverse=True)[1:6]

    recommendations_list = []
    recommendations_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommendations_poster.append(fetch_poster(movie_id))
        recommendations_list.append(movies.iloc[i[0]].title)

    return recommendations_list, recommendations_poster

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{movie_id}?api_key=0c6acee4e7092477848aceae26b2aeec&language=en-US'.format(movie_id=movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Which Movie would you like to recommend?',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations_list, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations_list[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations_list[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations_list[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations_list[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations_list[4])
        st.image(posters[4])