import requests
import streamlit as st
import pycountry
from keys import api_keys


st.header('MoBrian254 News App Demo')
st.text('This news app project uses NewsAPI, Streamlit, and PyCountry to allow it users \n'
        'to search for news articles by country and category. \n'
        'When a user types in a country and category, \n'
        'the app would use the NewsAPI to retrieve a list of articles that match the search criteria. \n'
        'Overall, this project would involve integrating multiple libraries and APIs to create \n'
        'a user-friendly news app that allows users to stay up-to-date with the latest news from around the world.')

col1, col2 = st.columns([3, 1])
with col1:
    c = st.text_input('Enter Country Name')

with col2:
    r = st.radio('Select a Topic', ('Technology', 'Finance', 'Agriculture', 'Business', 'Politics'))
    btn = st.button('Find')

if btn:
    country = pycountry.countries.get(name=c).alpha_2
    url = f"https://newsapi.org/v2/top-headlines?country={country}&pageSize=25&apiKey={api_keys}"
    res = requests.get(url)
    res = res.json()
    articles = res['articles']

    for article in articles:
        if article['urlToImage']:
            st.image(f"Image: {article['urlToImage']}")
        else:
            st.error('Image N/A')
        st.header(article['title'])

        if article['author']:
            st.write(f"Author: {article['author']}")

        st.write(f"published at: {article['publishedAt']}")
        st.write(f"Source: {article['source']['name']}")
        st.write(f"Click Link: {article['url']}")

        if article['description']:
            st.write(article['description'])


