import json

# Load JSON data from a file
with open("sample_data.json", "r") as file:
    data = json.load(file)

print("Current data:", data)

# update quality of the loaded data
data["quality"] = 99.2
print("Updated data:", data)

# save updated data back to the json file
with open("sample_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data is saved successfully :)")