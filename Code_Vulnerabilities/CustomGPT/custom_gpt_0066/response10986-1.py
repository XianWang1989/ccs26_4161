
import requests

# Define a mapping of country codes to common Accept-Language and Accept-Charset headers
country_headers = {
    'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'UTF-8'},
    'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251'},
    'FR': {'Accept-Language': 'fr-FR,fr;q=0.9', 'Accept-Charset': 'UTF-8'},
    # Add more countries as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    return data.get('country', None)

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code in country_headers:
        return country_headers[country_code]
    return {'Accept-Language': 'en-US', 'Accept-Charset': 'UTF-8'}  # Default headers

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP
default_headers = get_default_headers(ip)
print(default_headers)
