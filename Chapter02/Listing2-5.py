import dotenv
import os
import requests

dotenv.load_dotenv()  # Load variables from .env file
api_key = os.getenv("NASA_API_KEY")

# Use the key in your request
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)
print(response.json())
