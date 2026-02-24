import json
nested_json = '{"person":{"name":"aryan","age":18}}'
data = json.loads(nested_json)
print(data["person"]["name"])   