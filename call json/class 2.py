import json
data = {"roolno":23,"result":"fail"}
with open("class 2.json","w") as json_file:
    json.dump(data,json_file)