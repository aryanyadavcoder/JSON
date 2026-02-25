import json 
json_data = '{"rollno":45,"result":"fail"}'
data = json.loads(json_data)
print(data)