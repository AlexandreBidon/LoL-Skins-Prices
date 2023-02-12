import requests

url = 'http://0.0.0.0:8000'

champion_data = {
    "champion_id" : 4,
    "name" : "test test",
    "title" : "test def"
}

skin_data = {
    "champion_id":4,
    "skin_id":41,
    "name":"Skin test",
    "skin_num":1,
    "base_price":2000
}
# y = requests.get(url + '/management/reset')
# print(y.text)
# y = requests.post(url + '/champions', json = champion_data)
# print(y.text)
# y = requests.post(url + '/skins', json = skin_data)
# print(y.text)

x = requests.get(url + '/champions/all')
print(x.text)

x = requests.get(url + '/skins/all')
print(x.text)

x = requests.get(url + '/prices/history/skin_id=268005')
print(x.text)

x = requests.get(url + '/prices/current/skin_id=268005')
print(x.text)