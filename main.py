import streamlit as st
from src.scraper import scrape_website
from src.data_cleaning import clean_html
from src.llm_processing import process_with_llm

# ----------------- UI Design -----------------

# Header Section
st.title("🧠 AI Web Scraping Tool")
st.markdown("""
    This application allows you to scrape websites, clean the data, and use AI to summarize or extract insights. 
    Powered by Selenium, BeautifulSoup, and LLaMA. 
    """)

# Input Section
st.subheader("Enter Website Details")
url = st.text_input("🌐 Enter the website URL:", placeholder="https://example.com")

# Content type selection
content_type = st.multiselect(
    "📋 Select the content to scrape:", 
    ['Text', 'Images', 'Tables', 'Links'],
    help="Choose which types of content you'd like to extract from the webpage."
)

# Button Section
if st.button("🚀 Start Scraping"):
    if url:
        st.info("Scraping started... this might take a few moments.")
        with st.spinner("Scraping and processing..."):
            # Call scraper to get raw HTML
            raw_html = scrape_website(url)
            # Clean and process HTML
            cleaned_content = clean_html(raw_html, content_type)
            # Send cleaned content to AI for analysis
            ai_response = process_with_llm(cleaned_content)
        
        # Display results
        st.success("Scraping and AI processing complete!")
        st.subheader("🔍 Scraped and AI Processed Results:")
        st.write(ai_response)
    else:
        st.error("Please enter a valid URL.")
