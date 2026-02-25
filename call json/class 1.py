import json
data = {"roolno":45,"result":"pass"}
with open("class 1.json","w") as json_file:
    json.dump(data,json_file)