import requests

url = 'http://0.0.0.0:8000/champion'
myobj = {
    "champion_id" : 4,
    "name" : "test test",
    "title" : "test def"
}

x = requests.post(url, json = myobj)

print(x.text)