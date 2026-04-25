
import requests

# A simple mapping of country codes to default language and charset
country_language_mapping = {
    'US': ('en-US', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    # Add more countries as needed
}

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/country/')
    return response.text.strip()

def get_default_accept_headers(ip):
    country_code = get_country_code(ip)
    language, charset = country_language_mapping.get(country_code, ('en-US', 'UTF-8'))  # Default to US
    return language, charset

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
accept_language, accept_charset = get_default_accept_headers(ip_address)
print(f"Accept-Language: {accept_language}, Accept-Charset: {accept_charset}")
