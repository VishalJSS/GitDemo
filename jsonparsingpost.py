import requests
import json

add_book_response = requests.post('http://216.10.245.166/Library/Addbook.php', json={
    "name":"Learn Appium Auto"
    "isbn":"x235"
    "aisle":"275"
    "author":"john krasinsky"
}, headers={"Content-Type":"application/json"})

print(add_book_response.json())

response_addbook = add_book_response.json()
bookID = response_addbook['ID']