import requests
import json


response = requests.get("https://github.com/aryanyadavcoder/JSON/commit/ac20b933bf37255fc2adb5e9fef14064c6b48daa#diff-349fc861d3e742b8e4d71bf1dd4cc5ba2deecbff3b289857e2ff0f44196d2ecb")
data = response.json()
print(data)