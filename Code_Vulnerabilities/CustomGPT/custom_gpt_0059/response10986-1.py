
import requests

# Sample mapping of country codes to languages and charsets
COUNTRY_LANGUAGES = {
    'US': ('en-US', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'utf-8'),
    'DE': ('de-DE', 'utf-8'),
    'CN': ('zh-CN', 'utf-8'),
}

def get_country_code(ip):
    """Fetch the country code for the given IP."""
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    return response.json().get('country')

def get_default_language_and_charset(ip):
    """Determine the default Accept-Language and Accept-Charset for an IP."""
    country_code = get_country_code(ip)
    if country_code in COUNTRY_LANGUAGES:
        return COUNTRY_LANGUAGES[country_code]
    return ('en-US', 'utf-8')  # Default to English if not found

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP
language, charset = get_default_language_and_charset(ip_address)
print(f'Default Accept-Language: {language}, Accept-Charset: {charset}')
