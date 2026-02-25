import json
data = {"roolno":4,"result":"pass"}
with open("class 3.json","w") as json_file:
    json.dump(data,json_file)