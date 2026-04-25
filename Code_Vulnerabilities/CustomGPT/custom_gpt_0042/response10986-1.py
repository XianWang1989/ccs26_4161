
from geopy.geocoders import Nominatim
import requests

# Dictionary mapping country codes to default Accept-Language and Accept-Charset values
country_settings = {
    'US': ('en-US,en;q=0.9', 'UTF-8'),
    'RU': ('ru-RU,ru;q=0.9', 'windows-1251'),
    'DE': ('de-DE,de;q=0.9', 'UTF-8'),
    # Add more country codes as needed
}

def get_country_code(ip):
    """Get country code based on IP address."""
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country')

def get_default_headers(ip):
    """Get default Accept-Language and Accept-Charset based on IP address."""
    country_code = get_country_code(ip)
    if country_code in country_settings:
        return country_settings[country_code]
    return ('en-US,en;q=0.9', 'UTF-8')  # Default to English if country not found

# Example usage
ip_address = 'your_ip_address_here'  # Replace with the user's IP address
accept_language, accept_charset = get_default_headers(ip_address)

print(f'Accept-Language: {accept_language}')
print(f'Accept-Charset: {accept_charset}')
