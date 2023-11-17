import requests
try:
    response = requests.get('http://example.com')
    exit(0 if response.status_code == 200 else 1)
except:
    exit(1)
