
import requests

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    if response.status_code == 200:
        data = response.json()
        return data.get('country')
    return None

def get_default_language_and_charset(country_code):
    # Mapping of country codes to default Accept-Language and Accept-Charset
    lang_charset_mapping = {
        'US': ('en-US', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'DE': ('de-DE', 'UTF-8'),
        'FR': ('fr-FR', 'UTF-8'),
        # Add more mappings as needed
    }
    return lang_charset_mapping.get(country_code, (None, None))

def determine_accept_language(ip):
    country_code = get_country_code(ip)
    if country_code:
        language, charset = get_default_language_and_charset(country_code)
        return language, charset
    return None, None

# Example usage
ip_address = '8.8.8.8'  # Replace with actual IP
language, charset = determine_accept_language(ip_address)
print(f'Default Accept-Language: {language}, Accept-Charset: {charset}')
