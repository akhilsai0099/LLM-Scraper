from fastapi import FastAPI, Depends
from pydantic import BaseModel
from database import get_db, ScrapeHistory, SessionLocal
from sqlalchemy.orm import Session
from scrape import clean_body_content, extract_body_content, scrapeWeb
	

class HistoryRequest(BaseModel):
	url:str



app = FastAPI()

@app.get('/history')
def history(db: Session = Depends(get_db)):
	scrape_history = db.query(ScrapeHistory).all()
	return {"scrape_history":scrape_history}

@app.post('/scrape')
def scrape(req:HistoryRequest):
	html = scrapeWeb(req.url)
	body = extract_body_content(html)
	clean_body = clean_body_content(body)
	# db = SessionLocal()
	# scrape_history = ScrapeHistory(url=req.url)
	# db.add(scrape_history)
	# db.commit()
	# db.close()

	return {"page_data": clean_body}
