import os
import time
import requests

name = os.getenv('G', 'Lorenzo')

while True:
    print(f'Hello, {name}!')
    response = requests.get('http://example.com')
    print(f'Request Status: {response.status_code}')
    time.sleep(10)
