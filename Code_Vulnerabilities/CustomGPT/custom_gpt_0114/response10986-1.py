
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    if response.status_code == 200:
        data = response.json()
        return data.get('country', '')
    return None

# Function to map country code to default language and charset
def get_default_language_and_charset(country_code):
    language_charset_map = {
        'US': ('en-US', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'CN': ('zh-CN', 'UTF-8'),
        'FR': ('fr-FR', 'UTF-8'),
        # Add more mappings as needed
    }

    return language_charset_map.get(country_code, ('en', 'UTF-8'))  # Default to English

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
country_code = get_country_code(ip_address)
default_language, default_charset = get_default_language_and_charset(country_code)

print(f'Default Accept-Language: {default_language}')
print(f'Default Accept-Charset: {default_charset}')
