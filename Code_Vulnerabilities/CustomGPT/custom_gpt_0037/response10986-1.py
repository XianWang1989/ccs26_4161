
import requests

# Dictionary mapping country codes to common languages and charsets
country_language_map = {
    'US': ('en-US', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'DE': ('de-DE', 'utf-8'),
    'FR': ('fr-FR', 'utf-8'),
    # Add more mappings as needed
}

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    if response.status_code == 200:
        data = response.json()
        return data.get('country', '')
    return None

def get_default_language_and_charset(ip):
    country_code = get_country_code(ip)
    if country_code in country_language_map:
        return country_language_map[country_code]
    return ('en-US', 'utf-8')  # Default fallback

# Example usage
ip_address = '8.8.8.8'  # Replace with user's IP address
language, charset = get_default_language_and_charset(ip_address)
print(f'Default Accept-Language: {language}, Accept-Charset: {charset}')
