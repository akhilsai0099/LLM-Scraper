from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def scrapeWeb(url):
	print("Launching Chrome")
	options = webdriver.ChromeOptions()
	options.add_argument('--no-sandbox')
	options.add_argument('--headless=new')
	options.add_argument('--disable-dev-shm-usage')
	chromeDriverPath= './chromedriver'
	# chromeDriverPath= ''
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
	try:
		driver.get(url)
		time.sleep(10)
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