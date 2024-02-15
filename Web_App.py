import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import altair as alt

st.header('Spotify\'s Top Popular Songs For 2023', divider='rainbow')          
''' 
# Introduction

#### Objective & Project's Scope
* State Initial Questions
* Excercise Basic Data Preprocessing & EDA on the Dataset
* Share Insights and Findings
* Curate and Develop a Web Application Based on the Dataset
* Deploy the Application to Render

#### Initial Questions:
* Can we identify variables of interest that can be used to predict whether or not a song will make it the top 50, top 100, top 500? 
* According to the dataset, is there an apparent formula (i.e. "music magic") to making a good, catchy song ?
* Which top 10, 5, 3 artists has the most songs produced this year?
* Do these top artists have a similiar music magic formula that's allowing them to be in the top charts?

'''

check = st.checkbox('Click Here')
st.write('Did this Visual Display Correctly? Click the checkbox above', check)

if check:
    st.write(":sunglasses:"*6)

#                      ---------------- START THE ACTUAL PROJECT HERE ----------------


'''### Loading the Dataset'''

df = pd.read_csv("spotify-2023.csv", encoding='latin1')
st.dataframe(df)
st.write( '##### Spotify\'s Raw Dataset size is (953, 24)')



'''### Data Preprocessing '''
st.table(df.iloc[0:10])

st.write(df.info()) ## Can't seem to get this to display a info table on streamlit

'''Here we can see there are a few missing values located in 2 columns: *In Shazam Charts* and *Key* '''
st.table(df.isnull().sum())

''' 
After discovering the NaN values and in order to ensure the shape of the data is more uniform, 
removing NaN values would be the best option so the data becomes more sensible. Given that majority 
of the charting songs relatively had a value in each column compared to the songs that did have 
a column or two missing values there.
'''

st.table(df.dropna(inplace=True)) ## Can't seem to get this to display a info table on streamlit
st.table(df.info()) ## Can't seem to get this to display a info table on streamlit

'''
Here are the 11 unique keys that popular songs were played in all of 2023:
'''
st.table(df['key'].unique())

'''
There are **46** _distinct years_ a song was released in yet was relevant all of 2023 (that's wild!):
'''
st.table(df['released_year'].unique())

st.write('After re-shaping the dataframe and exploring other columns for unique insight, ' 
        'I believe now we can progress onward knowing the data is sensible.')


##                       ---------------- EVERYTHING FROM ABOVE IS GREAT ----------------


''' 
## Exploring the Data
Now we have our refined dataframe's head:
'''
df.head() ## Can't seem to get this to display a info table on streamlit

music_magic = df[['artist(s)_name','track_name','streams', 'released_year','bpm', 'key', 'mode', 'danceability_%','valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%']]
st.dataframe(music_magic)

''' 
## :zap: 2023 Lightning Spotify Facts :zap:

### Who has the most songs charting all of this year?
''' 


st.write(
    'There are **571 artists and or groups** who reached Spotify\'s Most Streams Songs on their platform in 2023. ' 
    'Yet there are **8 solo artists and 2 (Kpop & Duo) groups** that had **7-29 popular songs charting on Spotify.**'
    )


st.write ('As as we can see we have a female solo artist in #1: **Taylor Swift with 29 songs** and last but not least, '
          'two male groups with BTS and Drake & 21 Savage equally churning out 7 songs that dominated this year\'s charts.')
# Top Artist Bar Chart -- Great
top_artists = music_magic['artist(s)_name'].value_counts().head(10)
fig = px.bar(top_artists, labels={'Artist(s) Name'}, height=400)
st.write(fig)


st.write ('Although the duo, Tyler and Kali\'s _See You Again_ song killed it by making it to the top 10 charts, '
          'another duo, Archangel & Bizarrap\'s _Archangel: Bzrp Music Sessions Vol.54_ was reigning supreme '
          'this year by making it to number one in the top 10.'
          )

# Top Songs Bar Chart -- Okay BUT Idk which encoding character to use to correct the wonky text T-T, let alone the inability of the method actually ascending my values correctly
top_songs = music_magic.sort_values(by='streams', ascending=True).reset_index(drop=True)
top10 = top_songs.loc[0:10]
st.bar_chart(top10, x='track_name', y='streams', color='track_name')


st.write ('When considering Music Magic, does Speech have an impact?')

# Histogram: Streams Vs Speechiness -- Good
fig = px.histogram(df, x='streams', y='speechiness_%', histfunc='avg')
st.write(fig)


st.write ('When it comes to valance some times, it\'s straightforward or at times it\'s a paradox depending on the lyrics, yknow!')

# Histogram: Streams Vs Valence -- Good
fig = px.histogram(df, x='streams', y='valence_%', histfunc='avg')
st.write(fig)


st.write ('But now, what if we were to consider other elements in tandem with Valence, such as Energy and BPM?')

# Scatterplot: Energy Vs  BPM & Valance -- Good
fig = px.scatter_matrix(df, dimensions=["energy_%", "bpm", "valence_%"])
st.write(fig)



st.write ('Or what about: Valance VS Danceability and BPM?')

# Scatterplot: Danceability Vs  BPM & Valance -- Good
fig = px.scatter_matrix(df, dimensions=["danceability_%", "bpm", "valence_%"])
st.write(fig)


st.header(':green[Conclusion]')

'''

In conclusion, All in all, Taylor swift shows a clear indicator that she knows how to wield her popularity power to
stay reign over the Spotify domain. Furthermore, there are some apparent signs on how some artists rise and stay amongst the cream of the crop as they've crafted their
own form of Music Magic. Relatively most songs share these keys in each tier {insert here for each top 50/100/500}, as for energy and
BPM both of these elements are truly what drives a lot of artist and their specific genre they reside in as must artists average
{insert metrics for energy here} for energy and {insert metrics for BPM here} for BPM.

'''