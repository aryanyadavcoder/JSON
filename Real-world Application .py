import requests
import json


response = requests.get("https://aryanyadavcoder.github.io/JSON/Data.json")
data = response.json()
print(data)
