import requests
import json


response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Lucknow&appid=YOUR_KEY")
data = response.json()