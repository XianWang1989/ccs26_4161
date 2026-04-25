
import requests

# Mapping of country codes to default Accept-Language and Accept-Charset
country_language_mapping = {
    'US': ('en-US', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    # Add more mappings as needed
}

def get_country_code(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    if response.status_code == 200:
        data = response.json()
        return data.get('countryCode')
    return None

def get_default_language(ip):
    country_code = get_country_code(ip)
    if country_code in country_language_mapping:
        return country_language_mapping[country_code]
    return ('en', 'UTF-8')  # Default fallback

# Example usage
ip_address = '8.8.8.8'  # Replace with the target IP address
language, charset = get_default_language(ip_address)
print(f'Default Language: {language}, Default Charset: {charset}')
