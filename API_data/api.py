import requests
import json
import string

def download(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Błąd podczas pobierania danych: {response.status_code}")
        return None

url_api = "https://www.thecocktaildb.com/api/json/v1/1/search.php?f="


letters = list(string.ascii_lowercase) + list(string.digits)
print(letters[23])
json_data = []
for i in letters:
    url = url_api + i
    drinks = download(url)
    json_data.append(drinks)

if json_data:
    with open('data.json', 'w') as f:
        json.dump(json_data, f)
else:
    print("Nie udało się pobrać danych z API.")
