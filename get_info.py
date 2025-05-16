
import requests
import requests_cache

# Set up cache with 1-hour expiration (you can change this)
requests_cache.install_cache('alpha_vantage_cache', expire_after=3600)

# Overview request
url1 = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=DI6F9U0V14CL16IW'
r1 = requests.get(url1)
data1 = r1.json()

print("Overview data (from cache:", r1.from_cache, "):")
print(data1)

# Top Gainers/Losers request
url2 = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=DI6F9U0V14CL16IW'
r2 = requests.get(url2)
data2 = r2.json()

print("\nTop Gainers/Losers data (from cache:", r2.from_cache, "):")
print(data2)