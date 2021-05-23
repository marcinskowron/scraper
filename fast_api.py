from fastapi import FastAPI
import scraper

app = FastAPI()

@app.get("/keywords")
async def keywords_scraper(url: str):
    keywords = ','.join(scraper.get_keywords(url))
    return {"message": keywords}
