
import requests

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    return data.get('country')

def get_default_language_and_charset(country_code):
    language_mapping = {
        'US': ('en-US', 'UTF-8'),
        'GB': ('en-GB', 'UTF-8'),
        'FR': ('fr-FR', 'UTF-8'),
        'DE': ('de-DE', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'CN': ('zh-CN', 'UTF-8'),
        # Add more country mappings as needed
    }
    return language_mapping.get(country_code, ('en', 'UTF-8'))  # Default to English

def get_accept_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code:
        language, charset = get_default_language_and_charset(country_code)
        return {
            'Accept-Language': language,
            'Accept-Charset': charset
        }
    else:
        return None

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
headers = get_accept_headers(ip_address)
if headers:
    print("Default Accept headers:", headers)
else:
    print("Could not determine headers.")
