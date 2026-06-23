

import requests

response = requests.get(api_url)


def fetch_repository_data(api_url):
    try:
        response = requests.get(api_url , timeout = 5)

        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException:
        return None

    






