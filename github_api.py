
from utils import build_api_url


import requests


def fetch_repository_data(api_url):
    try:
        response = requests.get(api_url , timeout = 5)

        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException:
        return None

  
def fetch_contributors(owner , repo):
    base_url = build_api_url(owner , repo) 
    contributors_url = f"{base_url}/contributors"

    try :
        response = requests.get(contributors_url , timeout= 5)

        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException:
        return None


      







