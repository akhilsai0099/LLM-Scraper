from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def scrapeWeb(url):
	print("Launching Chrome")
	options = webdriver.ChromeOptions()
	options.add_argument('--headless=new')
	chromeDriverPath= './chromedriver.exe'
	driver = webdriver.Chrome(service=Service(chromeDriverPath),options=options)
	try:
		driver.get(url)
		html = driver.page_source
		print("Grabbed Page")
		return html
	finally:
		driver.close()

def extract_body_content(html):
	soup = BeautifulSoup(html, "html.parser")
	body = soup.body
	if body:
		return str(body)
	return ""

def clean_body_content(body_content):
	soup = BeautifulSoup(body_content, 'html.parser')
	for style_or_script in soup(['style','script']):
		style_or_script.extract()
	cleaned_content = soup.get_text(separator='\n')
	cleaned_content = '\n'.join([line.strip() for line in cleaned_content.splitlines() if line.strip()])
	return cleaned_content

def batch_content(body_content, limit = 6000):
	return [
		body_content[i:i+limit] for i in range(0,len(body_content),limit)
	]