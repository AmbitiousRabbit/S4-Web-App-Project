import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import altair as alt

st.header('Spotify\'s Top Popular Songs For 2023', divider='rainbow')          
st.header(':green[My Software Dev Project] - Sprint 4')

df = pd.read_csv("spotify-2023.csv", encoding='latin1')

#Test Visual 1

check = st.checkbox('Click Here')
st.write('Did this Visual Display Correctly? Click the checkbox below', check)

if check:
    st.write(":sunglasses:"*6)


fig = px.histogram(df, x='streams', y='speechiness_%', histfunc='avg')
st.write(fig)

fig = px.scatter_matrix(df, dimensions=["energy_%", "bpm", "valence_%"])
st.write(fig)


st.header('TripleTen Project')

