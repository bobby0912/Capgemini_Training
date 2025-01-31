import json

data={"name"="alice":"age"=30}
json_data=json.dumps(data)
print("json data: ",json_data)

parsed_data=json.loads(json_data) 
print("parsed data: "parsed_data)

while open("data.json"):
    pass 