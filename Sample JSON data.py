import json
json_data = '{"name": "Alice", "age": 28, "is_student": false}'
data = json.loads(json_data)
print(data["age"])
print(type(data))
