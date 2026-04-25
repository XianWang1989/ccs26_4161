
import requests

# Mapping of country codes to default Accept-Language and Accept-Charset
country_language_map = {
    'US': ('en-US', 'utf-8'),
    'FR': ('fr-FR', 'utf-8'),
    'DE': ('de-DE', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'CN': ('zh-CN', 'utf-8'),
    # Add more mappings as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/country/')
    return response.text.strip() if response.status_code == 200 else None

def get_default_language(ip_address):
    country_code = get_country_code(ip_address)
    if country_code in country_language_map:
        return country_language_map[country_code]
    else:
        return ('en', 'utf-8')  # Default to English if country is unknown

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP address
language, charset = get_default_language(ip)
print(f'Default Accept-Language: {language}, Accept-Charset: {charset}')
