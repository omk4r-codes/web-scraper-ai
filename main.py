# 1. create a simple streamlit app
# 2. create a function to extract transcriptions
# 3. create a function to summarize the transcriptions
# 4. create a function to display the summary   

import streamlit as st

st.title("AI Web Scraper")
url = st.text_input("Enter URL")
if st.button("Scrape"):
    st.write("Scraping...")