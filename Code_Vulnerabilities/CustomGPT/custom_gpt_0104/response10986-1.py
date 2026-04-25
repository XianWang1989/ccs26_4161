
import requests

# Example mapping of country codes to popular Accept-Language and Accept-Charset headers
default_headers = {
    'US': ('en-US', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'DE': ('de-DE', 'utf-8'),
    'FR': ('fr-FR', 'utf-8'),
    # Add more mappings as needed
}

def get_country_code(ip_address):
    # Using a geolocation API to get country code
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    return response.json().get('country', 'Unknown')

def get_default_accept_headers(ip_address):
    country_code = get_country_code(ip_address)

    return default_headers.get(country_code, ('en-US', 'utf-8'))  # Fallback to US defaults

# Usage example
ip_address = '8.8.8.8'  # Example IP address
language, charset = get_default_accept_headers(ip_address)
print(f"Default Accept-Language: {language}, Accept-Charset: {charset}")
