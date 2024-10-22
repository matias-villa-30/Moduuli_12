import requests

api = "https://api.chucknorris.io/jokes/random"

response = requests.get(api)

if response.status_code == 200:
    chiste = response.json()

    print(chiste["value"])
else:
    print(f"Error: {response.status_code}")
