
import requests

# Example mapping of country codes to default Accept-Language and Accept-Charset
country_language_map = {
    'US': ('en-US', 'UTF-8'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'JP': ('ja-JP', 'UTF-8'),
    # Add more countries as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/country/')
    return response.text.strip()

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    language, charset = country_language_map.get(country_code, ('en-US', 'UTF-8'))  # default to US
    return {
        'Accept-Language': language,
        'Accept-Charset': charset
    }

# Example usage
ip_address = '8.8.8.8'  # Example IP
default_headers = get_default_headers(ip_address)
print(default_headers)
