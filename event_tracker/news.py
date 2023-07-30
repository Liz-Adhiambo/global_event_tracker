import requests

def fetch_global_news():
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {
        "query": "domain:news",
        "mode": "timelinevolinfo",
        "TIMELINESMOOTH": "5",
        "FORMAT": "json",
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("timeline", [])