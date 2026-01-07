import requests

SYMBOL = "AAPL"
URL = f"https://finnhub.io/api/v1/quote?symbol={SYMBOL}&token=YOUR_API_KEY"

def get_price():
    response = requests.get(URL)
    data = response.json()
    print(f"Stock: {SYMBOL}")
    print("Current price:", data.get("c"))

if __name__ == "__main__":
    get_price()
