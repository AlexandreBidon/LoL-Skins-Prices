# API ENDPOINTS

[GO BACK TO HOME](../README.md)

The api features endpoints in the following categories :
- [Champions](#champions-endpoints)
- [Skins](#skins-endpoints)
- [Skin Price](#skin-price-endpoints)
- [Users](#users-endpoints)
- [Management](#management-endpoints)

**Note**: All the examples featured in this section require the package `requests`. You can import this package using the following command :
```python
import requests
```
## Champions endpoints

### List all champions
**Endpoint type : GET**

This endpoint lists all the champions that are present in the database. It is available at the following address 
> /champions/all

#### Example
Here is a code example to use this endpoint. You have to replace the URL with the URL of the API (usually http://0.0.0.0:8000).

```python
url=#Specify the API address here
result = requests.get(url + '/champions/all')
print(result.text)
```
### Show a champion
**Endpoint type : GET**

This endpoint shows a specific champion. It is available at the following address. You have to provide the id of the champion you want to see.
> /champions/{id}

#### Example
Here is a code example to use this endpoint. You have to replace the URL with the URL of the API (usually http://0.0.0.0:8000). You also have to add the `champion_id`.

```python
url=#Specify the API address here
champion_id=#Specify the id of the champion you want to see
result = requests.get(url + '/champions/' + champion_id)
print(result.text)
```
### Create a champion
**Endpoint type : POST**

This endpoint is used to create a new champion. It is available at the following address. You have to send some data explaining the new champion.
> /champions

The data sent must be in the following format :
```json
{
    "champion_id" : int,
    "name" : string,
    "title" : string
}
```
#### Example
Here is a code example to use this endpoint. You have to replace the URL with the URL of the API (usually http://0.0.0.0:8000).
```python
url=#Specify the API address here
champion_data = {
    "champion_id" : 24,
    "name" : "Jax",
    "title" : "Maître d'armes"
}
result = requests.post(url + '/champions/', json = champion_data)
print(result.text)
# If the result is {success : True} then the champion was added.
# You can then see the champion
result = requests.post(url + '/champions/all')
print(result.text)
```
### Delete a champion
**Endpoint type : DELETE**

This endpoint is used to delete a specific champion. It is available at the following address. You have to provide the id of the champion you want to delete.
> /champions/{id}

#### Example
Here is a code example to use this endpoint. You have to replace the URL with the URL of the API (usually http://0.0.0.0:8000). You also have to add the `champion_id`.

```python
url=#Specify the API address here
champion_id=#Specify the id of the champion you want to delete
result = requests.delete(url + '/champions/' + champion_id)
print(result.text)
```
#### Example

## Skins endpoints

## Skin Price endpoints

## Users endpoints

## Management endpoints