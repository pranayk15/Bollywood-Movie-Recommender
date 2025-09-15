import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    index=df[df['title']==movie].index[0]
    distances=similarity[index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_list=[]
    recommended_poster=[]
    for i in movies_list:
        recommended_list.append(df.iloc[i[0]].title)
        recommended_poster.append(df.iloc[i[0]].poster_path)
    return recommended_list,recommended_poster


st.header("Movie Recommender System")
df=pd.read_pickle(open('movie_list.pkl','rb'))
similarity=pd.read_pickle(open('similarity.pkl','rb'))
movie_list=df['title'].values
poster_path=df['poster_path'].values
# st.text(poster_path)
selected_movie=st.selectbox("Select a movie for recommendation: ",movie_list)

if st.button('Recommend'):
    recommended_movie,recommended_poster=recommend(selected_movie)
    # st.text(recommended_poster)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.write(recommended_movie[0])
        st.image(recommended_poster[0])
    with col2:
        st.write(recommended_movie[1])
        st.image(recommended_poster[1])
    with col3:
        st.write(recommended_movie[2])
        st.image(recommended_poster[2])
    with col4:
        st.write(recommended_movie[3])
        st.image(recommended_poster[3])
    with col5:
        st.write(recommended_movie[4])
        st.image(recommended_poster[4])

