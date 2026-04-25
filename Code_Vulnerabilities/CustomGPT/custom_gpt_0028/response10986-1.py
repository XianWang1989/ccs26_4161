
import requests

# Sample mapping of country codes to default Accept-Language and Accept-Charset
country_language_map = {
    'US': ('en-US', 'utf-8'),
    'FR': ('fr-FR', 'iso-8859-1'),
    'DE': ('de-DE', 'iso-8859-1'),
    'RU': ('ru-RU', 'windows-1251'),
    'CN': ('zh-CN', 'utf-8'),
    # Add more mappings as needed
}

def get_country_code(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()
    return data.get('countryCode')

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code in country_language_map:
        accept_language, accept_charset = country_language_map[country_code]
        return {
            'Accept-Language': accept_language,
            'Accept-Charset': accept_charset
        }
    else:
        return {
            'Accept-Language': 'en-US',
            'Accept-Charset': 'utf-8'
        }

# Example usage
ip = '8.8.8.8'  # Replace with the IP you want to check
headers = get_default_headers(ip)
print(headers)
