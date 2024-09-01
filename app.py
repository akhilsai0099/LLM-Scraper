import streamlit as st
from scrape import batch_content, clean_body_content, extract_body_content, scrapeWeb
from bs4 import BeautifulSoup

st.title("AI web Scraper")
url = st.text_input("Enter a Website URL")

if st.button("Scrape Site" ):
	html = scrapeWeb(url)
	body = extract_body_content(html)

	clean_body = clean_body_content(body)
	batched = batch_content(clean_body)
	st.write(batched)


