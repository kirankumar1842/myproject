import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
def get_response():
    resp = requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())
id=input("enter id:")
get_response()