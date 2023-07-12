import requests
import json
import os
os.system("cls")
Description = input('Description: ')
token = input('X-Session-Token: ')
headers = {
    "X-Session-Token": token
}
response = requests.get('https://api.revolt.chat/users/dms', headers=headers)
group_ids = []
response_data = json.loads(response.text)
for item in response_data:
    if item['channel_type'] == 'Group':
        group_ids.append(item['_id'])
json_data = {
    'description': Description,
    'nsfw': False,
}
for group_id in group_ids:
    response = requests.patch(f'https://app.revolt.chat/api/channels/{group_id}', headers=headers, json=json_data)
    os._exit(0)