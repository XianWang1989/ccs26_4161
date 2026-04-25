
from geopy.geocoders import Nominatim
import requests

# Mapping of country codes to common language/charsets
country_language_map = {
    'US': ('en-US', 'utf-8'), 
    'FR': ('fr-FR', 'iso-8859-1'),
    'DE': ('de-DE', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    # Add more mappings as needed
}

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country')

def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in country_language_map:
        return country_language_map[country_code]
    else:
        return ('en-US', 'utf-8')  # Default fall-back

# Example usage
ip_address = 'YOUR_IP_ADDRESS_HERE'  # Replace with a valid IP address
language, charset = get_default_headers(ip_address)

print(f'Default Accept-Language: {language}')
print(f'Default Accept-Charset: {charset}')
