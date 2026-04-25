
import requests

# This function retrieves the country code based on the IP address
def get_country_code(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()
    return data.get('countryCode')

# This function returns the default headers based on the country code
def get_default_headers(country_code):
    headers_mapping = {
        'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'UTF-8'},
        'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251'},
        'DE': {'Accept-Language': 'de-DE,de;q=0.9', 'Accept-Charset': 'ISO-8859-1'},
        # Add more country codes and their respective headers here
    }
    return headers_mapping.get(country_code, {'Accept-Language': 'en', 'Accept-Charset': 'UTF-8'})

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP address
country_code = get_country_code(ip)
default_headers = get_default_headers(country_code)

print(f'Default Headers for IP {ip}: {default_headers}')
