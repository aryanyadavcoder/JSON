import json
with open("data.json","r") as json_file:
    data = json.load(json_file)
    data["no "] = "4"
with open("data.json","w") as json_file:
    json.dump(data,json_file)       