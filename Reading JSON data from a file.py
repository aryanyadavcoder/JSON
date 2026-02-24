import json
data = {"fruit":"apple","color":"red"}
with open("data.json","r") as json_file:
    loaded_data=json.load(json_file)
    print(loaded_data["color"])