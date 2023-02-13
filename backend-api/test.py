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

user_data = {
    "name": "Alexandre",
    "mail" : "alexandre.bidon.44@gmail.com",
    "skin_list" : [268005,268004]
}

new_price = [
    {
        "skin_id" : 268005,
        "new_price" : 500
    },
    {
        "skin_id" : 268004,
        "new_price" : 500
    },
    {
        "skin_id" : 245001,
        "new_price" : 500
    }    
]
# y = requests.get(url + '/management/reset')
# print(y.text)
# y = requests.post(url + '/champions', json = champion_data)
# print(y.text)
# y = requests.post(url + '/skins', json = skin_data)
# print(y.text)

y = requests.post(url + '/users', json = user_data)
print(y.text)

x = requests.get(url + '/champions/all')
print(x.text)

x = requests.get(url + '/skins/all')
print(x.text)

x = requests.get(url + '/prices/history/skin_id=268005')
print(x.text)

y = requests.post(url + '/prices', json = new_price)
print(y.text)

x = requests.get(url + '/prices/history/skin_id=268005')
print(x.text)
