import streamlit as st
from scrape import batch_content, clean_body_content, extract_body_content, scrapeWeb
from parser import parse_with_llm
import requests
import json
st.title("AI web Scraper")

url = st.text_input("Enter a Website URL")

if st.button("Scrape Site"):
	with st.spinner("Please Wait while we fetch the page"):
		headers = {"Content-Type": "application/json"}
		data = json.dumps({"url":url})
		res = requests.post('https://llm-scraper.onrender.com/scrape',data=data,headers=headers)
		

	if res.status_code == 200:
		st.session_state.body_content = res.json()['page_data']

	with st.expander("View Page Content"):
		st.text_area("Page Content", st.session_state.body_content, height=300)


if "body_content" in st.session_state:
	parse_desc = st.text_area("Enter What you want to parse in the website", height = 200)

	if st.button("Parse Content"):
		if parse_desc:
			with st.spinner("Parsing the Given Website"):
				dom_chunks = batch_content(st.session_state.body_content)
				res = parse_with_llm(dom_chunks,parse_desc)
				st.write(res)
