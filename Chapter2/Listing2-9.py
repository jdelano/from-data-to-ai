import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
print(response.status_code)

data = response.json()
print(data)
