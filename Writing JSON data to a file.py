import json
data = {"fruit":"apple","color":"red"}
with open("data.json","w") as json_file:
    json.dump(data,json_file)