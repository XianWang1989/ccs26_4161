
import requests

# Mapping of country codes to a default Accept-Language and Accept-Charset
language_map = {
    'US': ('en-US', 'UTF-8'),
    'FR': ('fr-FR', 'ISO-8859-1'),
    'DE': ('de-DE', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'CN': ('zh-CN', 'UTF-8'),
    # Add more mappings as needed
}

def get_language_by_ip(ip_address):
    # Get country code from IP
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')

    if response.status_code == 200:
        data = response.json()
        country_code = data.get('country')

        # Retrieve the default language and charset from the mapping
        accept_language, accept_charset = language_map.get(country_code, ('en', 'UTF-8'))
        return accept_language, accept_charset
    else:
        return 'en', 'UTF-8'  # Default values if the API call fails

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP address
language, charset = get_language_by_ip(ip)
print(f'Accept-Language: {language}, Accept-Charset: {charset}')
