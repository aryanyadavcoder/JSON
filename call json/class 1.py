import json
json_data = '{"rollno":5,"result":"pass"}'
data = json.loads(json_data)
print(data)