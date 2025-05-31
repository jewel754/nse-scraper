from fastapi import FastAPI
from scraper import get_nse_quote
import os

app = FastAPI()

@app.get("/quote/{ticker}")
async def quote(ticker: str):
    return get_nse_quote(ticker.upper())

@app.get("/peers/{ticker}")
async def peers(ticker: str):
    return {"message": "Peer scraping coming soon!"}

# Health check
@app.get("/")
async def root():
    return {"status": "Live"}