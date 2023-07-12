import requests
import time
import os
os.system("cls")
amount = input('Amount: ').strip()
amount = int(amount)
token = input('X-Session-Token: ')
name = input('Name: ')

headers = {
    'X-Session-Token': token,
}

data = {
    "name": name,
    "users": []
}

for x in range(amount):
    response = requests.post('https://app.revolt.chat/api/channels/create', headers=headers, json=data)
    print('successfully created group chat')
    if 'retry_after' in response.json():
        retry_after_ms = response.json()['retry_after']
        print (f'Ratelimited Sleeping for {retry_after_ms / 1000} seconds')
        time.sleep(retry_after_ms / 1000)
os._exit(0)