
import requests

# Sample mapping of country codes to default Accept-Language and Accept-Charset
country_language_map = {
    'US': ('en-US', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    # Add more countries as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = response.json()
    return data.get('country')

def get_default_accept_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code in country_language_map:
        return country_language_map[country_code]
    else:
        return ('en', 'UTF-8')  # Default to English if country not found

# Example use
ip_address = '8.8.8.8'  # Replace with the user's actual IP address
language, charset = get_default_accept_headers(ip_address)
print(f"Accept-Language: {language}, Accept-Charset: {charset}")
