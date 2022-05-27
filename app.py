# importing the required libraries..
import pickle
import streamlit as st
import requests

# helper function to fetch the movie posters that should be visible to the user :
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Main Function to generate the recommendation and get the top5 similar movies names along with their posters :
def recommend(movie):
    
    #getting the index..
    index = movies[movies['title'] == movie].index[0]

    #getting similarity distances..
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        # getting the id
        movie_id = movies.iloc[i[0]].movie_id

        #appending the posters and names to the recommendation lists
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


# Setting the header/ title of the Web page..
st.header('Movie Recommender System')

# Loading the movies and the similarity matrix..
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Generating a Drop-down Menu/ Dialog-box of movie titles,
# from where user can either type or select the input movie..
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the drop-down menu",
    movie_list
)

# Processing and Displaying the recommendations..
if st.button('Show Recommendation'):
    
    #fetching names and posters of recommended movies..
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    
    #dividing the display space into 5 columns for the 5 top movies..
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:                                               #represents top1 movie
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])

    with col2:                                               #represents top2 movie
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:                                               #represents top3 movie
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])

    with col4:                                               #represents top4 movie
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])

    with col5:                                               #represents top5 movie
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])


# --------------------------------------------- End -----------------------------------------------
# -------------------------------------------------------------------------------------------------


