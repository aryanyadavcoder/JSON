import json
json_string = '{"name":"invalid JSON","age":18}'
try:
    data  = json.loads(json_string)
    print(data)
    print(type(data))
except json.JSONDecodeError as e:
    print("errer",e)    