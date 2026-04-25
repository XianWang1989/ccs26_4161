
import requests

# Geolocation API to get country code from IP
API_URL = "http://ip-api.com/json/{}"

# Mapping of country codes to common Accept-Language headers
COUNTRY_LANG_MAP = {
    'US': 'en-US,en;q=0.5',
    'GB': 'en-GB,en;q=0.5',
    'FR': 'fr-FR,fr;q=0.5',
    'DE': 'de-DE,de;q=0.5',
    'RU': 'ru-RU,ru;q=0.5',
    # Add more country codes and their language preferences as needed
}

def get_country_from_ip(ip_address):
    response = requests.get(API_URL.format(ip_address))
    data = response.json()
    return data.get('countryCode')

def get_default_accept_language(ip_address):
    country_code = get_country_from_ip(ip_address)
    if country_code in COUNTRY_LANG_MAP:
        return COUNTRY_LANG_MAP[country_code]
    else:
        return 'en'  # Default fallback

# Example usage
ip = '8.8.8.8'  # Replace with the target IP address
default_language = get_default_accept_language(ip)
print(f"Default Accept-Language for IP {ip}: {default_language}")
