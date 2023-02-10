# API ENDPOINTS

[GO BACK TO HOME](../README.md)

The api features endpoints in the following categories :
- [Champions](#champions-endpoints)
- [Skins](#skins-endpoints)
- [Skin Price](#skin-price-endpoints)
- [Management](#management-endpoints)

**Note**: All the examples featured in this section require the package `requests`. You can import this package using the following command :
>import requests
## Champions endpoints

#### List all champions
This endpoint lists all the champions that are present in the database. It is availabe at the following address 
> /champions/all

##### Example
Here is a code exemple to use this endpoint. You have to replace the URL with the URL of the API (usually http://0.0.0.0:8000).

```python
url=#Specify the API address here
result = requests.get(url + '/champions/all')
print(result.text)
```
#### Show a champion
This endpoint shows a specific champion. It is availabe at the following address. You have to provide the id of the champion you want to see.
> /champions/{id}

##### Example
Here is a code exemple to use this endpoint. You have to replace the URL with the URL of the API (usually http://0.0.0.0:8000). You also have to add the `champion_id`.

```python
url=#Specify the API address here
champion_id=#Specify the id of the champion you want to see
result = requests.get(url + '/champions/' + champion_id)
print(result.text)
```
#### Create a champion

##### Example

#### Delete a champion

##### Example
## Skins endpoints

## Skin Price endpoints

## Management endpoints