import json
import requests

r=requests.get("http://localhost:3000")
data = r.json()


i=0
while i < len(data):
    name = data[i]["name"]
    color = data[i]["color"]

    print(f"{name.capitalize()} is {color}.")
    i +=1
