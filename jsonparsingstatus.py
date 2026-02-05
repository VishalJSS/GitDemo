import requests
import json

response=requests.get('http://216.10.245.166/Library/GetBook.php',params={'AuthorName':"Rahul Shetty2"},)
data_json=response.json()
print(type(data_json))
print(data_json)

print(data_json[0]["isbn"])
print(response.status_code)

assert response.status_code == 200

print(response.headers)

assert  response.headers['Content-Type'] == 'application/json;charset=UTF-8'