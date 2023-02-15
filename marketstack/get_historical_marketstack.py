import requests


params = {
    'access_key': "ae5ec54785ba702ff8c7cd36a76748a6",
    'limit': 1
}

response = requests.get('http://api.marketstack.com/v1/tickers/aapl/eod', params)

result = response.json()

print(result["data"])
# print(result["data"][0]["adj_open"])
# print(result["data"][0]["adj_open"])
