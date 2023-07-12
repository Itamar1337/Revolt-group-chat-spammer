import requests
import json
from threading import Thread
import os
os.system ("cls")
def dm_group(token, group_id, message):
    headers = {
        "X-Session-Token": token
    }
    json_data = {
        'content': message
    }
    response = requests.post(
        f'https://app.revolt.chat/api/channels/{group_id}/messages',
        headers=headers,
        json=json_data,
    )
    if response.status_code == 200:
        response_data = json.loads(response.text)
        message_id = response_data['_id']
        print(f'Sent message in group {group_id}. Message ID: {message_id}')
    else:
        print(f'Failed to send message in group {group_id}. Status code: {response.status_code}')

token = input('X-Session-Token: ')
message = input('Message: ')

headers = {
    "X-Session-Token": token
}

response = requests.get('https://api.revolt.chat/users/dms', headers=headers)
group_ids = []

response_data = json.loads(response.text)
for item in response_data:
    if item['channel_type'] == 'Group':
        group_ids.append(item['_id'])

while True:
    for group_id in group_ids:
        dm_group(token, group_id, message)
    os._exit(0)