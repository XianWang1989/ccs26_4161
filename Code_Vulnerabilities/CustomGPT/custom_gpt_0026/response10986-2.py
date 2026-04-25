
import requests

def get_country_code(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = response.json()
    return data.get('country')  # Returns the country code
