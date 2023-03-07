import requests

url = "http://10.67.78.3:8889/user/testuser2"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
