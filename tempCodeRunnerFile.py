import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
response.json()