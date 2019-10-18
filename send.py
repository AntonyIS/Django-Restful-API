import requests

headers = {}
headers['authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxMzcwODAyLCJqdGkiOiJjZGNkMDAyMDY2ZTM0NWY5YjY4YTQwZDEyM2IyZGE4ZiIsInVzZXJfaWQiOjF9.goIXnmx0faG2zQxxJwwF_3CzTFOz323hWzRnJ2TQRng'

req = requests.get('http://127.0.0.1:3000/paradigm',headers=headers)
print(req.text)