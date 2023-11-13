import json

# Read the existing JSON file
existing_file_path = './data.json'
with open(existing_file_path, 'r') as existing_file:
    data = json.load(existing_file)

# Read the new data from the separate JSON file
new_data_file_path = './new_data.json'
with open(new_data_file_path, 'r') as new_data_file:
    new_data = json.load(new_data_file)

# Append the new data to the "data" array
data["data"].append(new_data)

# Write the updated JSON back to the existing file
with open(existing_file_path, 'w') as existing_file:
    json.dump(data, existing_file, indent=2)
