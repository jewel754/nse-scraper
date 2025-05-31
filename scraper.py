from bs4 import BeautifulSoup
import requests

def get_nse_quote(ticker):
    url = f"https://www.nseindia.com/get-quotes/equity?symbol={ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract data (adjust selectors as needed)
        price = soup.select_one(".lastPrice").text
        pe = soup.select_one(".peRatio").text
        
        return {
            "ticker": ticker,
            "price": float(price.replace(',', '')),
            "pe_ratio": float(pe),
            "source": "NSE India"
        }
    except Exception as e:
        return {"error": str(e)}