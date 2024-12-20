import streamlit as st
from scrape import scrape_webpage

st.title("AI Web Scraper")
url = st.text_input("Enter URL")

if st.button("Scrape"):
    st.write("Scraping...")
    result = scrape_webpage(url)
    print(result)