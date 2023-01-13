import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"

todo = {
    "title": "Fah",
    }

response = requests.patch(api_url, json=todo)
print(response.json())
print(response.status_code)