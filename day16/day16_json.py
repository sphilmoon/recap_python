import json

#JSON string
json_data = '{"name": "Sample_001", "quality": 95.5, "reads": 229000}'

# parse json string to python dictionary 
data = json.loads(json_data)
print(data)
print(data["name"]) # accessing specific data

# loading json file
with open("sample.json", "r") as file:
    data2 = json.load(file)

print(data2)
print(data2["quality"]) 

# converting python dictionary to json
data3 = {
    "name": "Sample_001",
    "quality": 95.5,
    "reads": 100000
}
json_data = json.dumps(data3, indent=4)
print(json_data)

# write/save json data to a file
with open("output.json", "w") as file:
    json.dump(data3, file, indent=4)