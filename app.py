# Importing the required libraries
import streamlit as st
import pickle as pkl
import pandas as pd
import requests

# Loading the movies dataset obtained from our python code
movies = pkl.load(open('movies_list_with_posters.pkl', 'rb'))
movie_names = movies['title'].values

# Loading the similarity matrix obtained from our python code
similarity = pkl.load(open('similarity_matrix.pkl', 'rb'))

# Defining a function which would fetch the posters of the recommended movies
# def fetch_poster(movie_id):
#     response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=d2fc6a35bc87239dbfc789df27f83875&language=en-US')
#     data = response.json()
#     return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']

# Defining our main recommend function which would recommend users movies based on their selection on the website
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_data = movies.iloc[i[0]]
        recommended_movies.append(movie_data.title)
        recommended_posters.append(movie_data.poster_url)

    return recommended_movies, recommended_posters

# Displaying the title of our webpage
st.title('Movie Recommender System')

selected_movie = st.selectbox('Choose your favourite movie from the list below so that we can recommend you some more based on that!',
                              movie_names)

# Creating the recommend button which would return all the recommended movies
if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader(names[0])
        st.image(posters[0])

    with col2:
        st.subheader(names[1])
        st.image(posters[1])

    with col3:
        st.subheader(names[2])
        st.image(posters[2])

    with col4:
        st.subheader(names[3])
        st.image(posters[3])

    with col5:
        st.subheader(names[4])
        st.image(posters[4])