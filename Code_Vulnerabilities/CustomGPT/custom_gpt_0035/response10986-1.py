
import requests

# Mapping of country codes to default Accept-Language and Accept-Charset
country_languages = {
    'US': ('en-US', 'UTF-8'),
    'FR': ('fr-FR', 'ISO-8859-1'),
    'DE': ('de-DE', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    # Add more mappings as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    return data.get('country', '')

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    return country_languages.get(country_code, ('en-US', 'UTF-8'))  # Default to US if not found

# Example usage
ip_address = '8.8.8.8'  # Replace with the actual IP address
language, charset = get_default_headers(ip_address)
print(f"Default Accept-Language: {language}, Accept-Charset: {charset}")
