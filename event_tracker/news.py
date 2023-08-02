import requests

def get_gdelt_data():
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {
        "query": "domain:news",
        "mode": "timelinevolinfo",
        "TIMELINESMOOTH": "5",
        "FORMAT": "json",
    }
    response = requests.get(url, params=params)
    data = response.json()
    data=data['timeline'][0]
    data['data'][0]['toparts']
    
    return data