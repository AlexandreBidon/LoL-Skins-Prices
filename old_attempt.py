import requests

url = 'http://0.0.0.0:80'

user_data = {
    "name": "Alexandre",
    "mail" : "alexandre.bidon.44@gmail.com",
    "skin_list" : [268005,268004,245001,24005,24014,238003,238013]
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
    },
    {
        "skin_id" : 24005,
        "new_price" : 500
    },
    {
        "skin_id" : 24014,
        "new_price" : 500
    },
    {
        "skin_id" : 238003,
        "new_price" : 500
    },
    {
        "skin_id" : 238013,
        "new_price" : 500
    }  
]

# y = requests.post(url + '/users', json = user_data)
# print(y.text)

# x = requests.get(url + '/champions/all')
# print(x.text)


# x = requests.get(url + '/prices/history/skin_id=268005')
# print(x.text)

# y = requests.post(url + '/prices', json = new_price)
# print(y.text)

# x = requests.get(url + '/prices/history/skin_id=268005')
# print(x.text)

x = requests.get(url + '/skins/web')
print(x.text)
