import streamlit as st
from scrape import scrape_webpage, split_dom_content, clean_body_content, extract_body_content

st.title("AI Web Scraper")
url = st.text_input("Enter URL")

if st.button("Scrape"):
    st.write("Scraping...")
    result = scrape_webpage(url)
    print(result)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area("What do you want to parse?")
    if st.button("Parse"):
        if parse_description:
            st.write("Parsing...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
