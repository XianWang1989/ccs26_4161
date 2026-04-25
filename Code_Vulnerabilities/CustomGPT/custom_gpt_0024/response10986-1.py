
import requests

# Mapping of country codes to their most common Accept-Language and Accept-Charset
country_map = {
    'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'utf-8, windows-1252;q=0.9'},
    'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251, utf-8;q=0.9'},
    'DE': {'Accept-Language': 'de-DE,de;q=0.9', 'Accept-Charset': 'utf-8, iso-8859-1;q=0.9'},
    # Add more countries as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/country/')
    return response.text.strip()

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    headers = country_map.get(country_code, {'Accept-Language': 'en;q=0.8', 'Accept-Charset': 'utf-8'})
    return headers

# Example usage
ip = '8.8.8.8'  # Replace with the actual IP
default_headers = get_default_headers(ip)
print(f'Default Headers for IP {ip}: {default_headers}')
