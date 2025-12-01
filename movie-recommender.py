# Standard Imports
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv('dataset.csv')
movies['tags'] = movies['overview'].fillna('') + " " + movies['genre'].fillna('')

# Vectorization
cv = CountVectorizer(max_features=10000, stop_words='english')
vector = cv.fit_transform(movies['tags']).toarray()


# Compute similarity matrix
similarity = cosine_similarity(vector)


# Recommendation function
def recommend_movies(movie_title):
    if movie_title not in movies['title'].values:
        print("Movie not found.")
        return
    index = movies[movies['title'] == movie_title].index[0]
    distance = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:6]
    recommendations = []
    for i in distance:
        recommendations.append(movies.iloc[i[0]].title)
        print(movies.iloc[i[0]].title)
    
    return recommendations

# Example usage
recommend_movies("Iron Man 3")

import streamlit as st
st.title("🎬 Movie Recommender System")
st.write("Find movies similar to your favourites!")

# Dropdown or text input
movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", sorted(movie_list))

if st.button("Recommend"):
    recommendations = recommend_movies(selected_movie)

    st.subheader(f"Movies similar to **{selected_movie}**:")
    for i, movie in enumerate(recommendations, start=1):
        st.write(f"**{i}. {movie}**")
