import json
import requests
import os

# Define the GitHub repository details
repository_owner = 'gethushan'
repository_name = 'action-test'
existing_file_path = 'data.json'  # Path to the existing JSON file in the repository
new_data_file_path = 'new_data.json'  # Path to the new data JSON file in the repository
github_token = os.getenv('GITHUB_TOKEN')  # Access the GITHUB_TOKEN environment variable

# Define the URL to the GitHub raw JSON files
raw_existing_json_url = f'https://raw.githubusercontent.com/{repository_owner}/{repository_name}/main/{existing_file_path}'
raw_new_data_json_url = f'https://raw.githubusercontent.com/{repository_owner}/{repository_name}/main/{new_data_file_path}'

# Fetch the existing JSON data from the GitHub repository
response_existing = requests.get(raw_existing_json_url, headers={'Authorization': f'token {github_token}'})
response_new_data = requests.get(raw_new_data_json_url, headers={'Authorization': f'token {github_token}'})

if response_existing.status_code == 200 and response_new_data.status_code == 200:
    existing_data = json.loads(response_existing.text)
    new_data = json.loads(response_new_data.text)

    # Append the new data to the "data" array
    existing_data["data"].append(new_data)

    # Convert the updated data to JSON
    updated_data_json = json.dumps(existing_data, indent=2)

    # Update the GitHub file using the GitHub API
    update_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{existing_file_path}'
    update_payload = {
        "message": "Update JSON file",
        "content": updated_data_json,
        "sha": existing_data["data"],
    }
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    update_response = requests.put(update_url, headers=headers, json=update_payload)

    if update_response.status_code == 200:
        print("JSON file updated successfully on GitHub.")
    else:
        print(f"Failed to update JSON file on GitHub. Status Code: {update_response.status_code}")
else:
    print("Failed to fetch JSON data from GitHub.")
