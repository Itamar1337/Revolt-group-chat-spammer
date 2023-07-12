import requests
import json
import os
os.system("cls")
member = input('Member ID to add: ')
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
for group_id in group_ids:
    response = requests.put(f'https://app.revolt.chat/api/channels/{group_id}/recipients/{member}', headers=headers)
    print (f"added {member} to {group_id}")
os._exit(0)