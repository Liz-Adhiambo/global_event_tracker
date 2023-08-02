import requests

def get_gdelt_data(location=None, language=None):
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {
        "query": "domain:news",
        "mode": "timelinevolinfo",
        "TIMELINESMOOTH": "5",
        "FORMAT": "json",
    }

    if location:
        params["location"] = location

    if language:
        params["language"] = language

    response = requests.get(url, params=params)
    data = response.json()
    
    if 'timeline' in data and len(data['timeline']) > 0:
        return data['timeline'][0]
    else:
        return None