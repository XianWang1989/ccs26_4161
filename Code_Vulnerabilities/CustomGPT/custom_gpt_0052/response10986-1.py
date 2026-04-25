
import requests

# Example mapping of country codes to default Accept-Language and Accept-Charset
country_preferences = {
    'US': ('en-US', 'utf-8'),
    'GB': ('en-GB', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'DE': ('de-DE', 'utf-8'),
    # Add more countries as needed
}

def get_country_code(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()
    return data['countryCode'] if data['status'] == 'success' else None

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code in country_preferences:
        return country_preferences[country_code]
    return ('en', 'utf-8')  # Default to English if country is unknown

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
language, charset = get_default_headers(ip_address)
print(f'Default Accept-Language: {language}, Accept-Charset: {charset}')
