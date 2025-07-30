import requests

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2025-07-04"
response = requests.get(url)
data = response.json()

print(data["title"])
print(data["explanation"])
print(data["url"])
