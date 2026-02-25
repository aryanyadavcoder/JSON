import json 
json_data = '{"rollno":32,"result":"pass"}'
data = json.loads(json_data)
print(data)