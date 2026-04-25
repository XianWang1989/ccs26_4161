
import requests

# Mapping of country codes to default Accept-Language and Accept-Charset
country_language_mapping = {
    'US': ('en-US', 'UTF-8'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'CN': ('zh-CN', 'UTF-8'),
    # Add more country codes as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    if response.status_code == 200:
        data = response.json()
        return data.get('country')
    return None

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code:
        return country_language_mapping.get(country_code, ('en-US', 'UTF-8'))
    return ('en-US', 'UTF-8')  # Default fallback

# Example usage
ip_address = '8.8.8.8'  # Replace with the target IP
language, charset = get_default_headers(ip_address)
print(f'Default Accept-Language: {language}, Accept-Charset: {charset}')
