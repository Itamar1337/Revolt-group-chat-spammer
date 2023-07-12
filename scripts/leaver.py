import requests
import json
from threading import Thread
import os
os.system ("cls")
def leave_group(token, group_id):
    headers = {
        "X-Session-Token": token
    }
    response = requests.delete(f'https://app.revolt.chat/api/channels/{group_id}', headers=headers)
    if response.status_code == 204:
        print(f'Left: {group_id}')
    else:
        print(response.status_code)

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
count = len(group_ids)
print(f'Leaving {count} group chats...')

threads = []
for group_id in group_ids:
    t = Thread(target=leave_group, args=(token, group_id))
    threads.append(t)
    t.start()

for group in threads:
    group.join()
os._exit(0)