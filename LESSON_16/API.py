import requests
import json

api_response = requests.get('https://jsonplaceholder.typicode.com/todos')
print(api_response.status_code)
data = api_response.text
parse_json = json.loads(data)

print("Todos:", parse_json)

"""
An Application Programming Interface (API) is a web service that grants access
to specific data and methods that other applications can access – and sometimes edit – via standard HTTP protocols, just like a website. This simplicity makes it easy to quickly integrate APIs into a wide variety of applications. REpresentational State Transfer (REST), is probably the most popular architectural style of APIs for web services. It consists of a set of guidelines designed to simplify client / server communication.
REST APIs make data access much more straightforward and logical.
"""
