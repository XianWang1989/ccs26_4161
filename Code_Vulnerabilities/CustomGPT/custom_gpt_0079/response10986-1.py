
import requests

def get_country_from_ip(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data.get('country')

def get_default_accept_headers(country_code):
    # Mapping of country codes to default Accept-Language and Accept-Charset
    language_map = {
        'US': ('en-US', 'UTF-8'),
        'GB': ('en-GB', 'UTF-8'),
        'DE': ('de-DE', 'UTF-8'),
        'FR': ('fr-FR', 'UTF-8'),
        'RU': ('ru-RU', 'Windows-1251'),
        # Add more country codes and preferences as needed
    }
    return language_map.get(country_code, ('en', 'UTF-8'))  # Default if unknown

ip_address = '8.8.8.8'  # Example IP address to test
country_code = get_country_from_ip(ip_address)

if country_code:
    accept_language, accept_charset = get_default_accept_headers(country_code)
    print(f'Default Accept-Language: {accept_language}, Accept-Charset: {accept_charset}')
else:
    print("Could not determine country code.")
