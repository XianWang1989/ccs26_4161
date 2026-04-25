
import requests

# Function to get country code from IP
def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    return response.json().get('country')

# Mapping of country codes to common Accept-Language and Accept-Charset
country_language_map = {
    'US': ('en-US', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
}

# Function to get default language and charset
def get_default_language_charset(ip_address):
    country_code = get_country_code(ip_address)
    return country_language_map.get(country_code, ('en-US', 'UTF-8'))  # Fallback to English

# Example usage
ip = '8.8.8.8'  # Replace with the actual IP address
language, charset = get_default_language_charset(ip)
print(f'Default Accept-Language: {language}, Accept-Charset: {charset}')
