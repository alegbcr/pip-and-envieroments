import requests


def get_categories():
    res = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(res.status_code)
    print(res)
    print(res.text)
    print(type(res.text))
    categories = res.json()
    for category in categories:
        print(category["id"], category["name"])
