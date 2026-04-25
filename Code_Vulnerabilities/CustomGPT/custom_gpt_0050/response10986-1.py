
import requests

# Sample mapping of country codes to default Accept-Language and Accept-Charset
country_preferences = {
    'US': ('en-US', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'utf-8'),
    'DE': ('de-DE', 'utf-8'),
    # Add more country codes and their preferences as needed
}

def get_country_code(ip_address):
    # Use a free IP geolocation API
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    if response.status_code == 200:
        data = response.json()
        return data.get('country', 'Unknown')
    return None

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code and country_code in country_preferences:
        lang, charset = country_preferences[country_code]
        return {
            'Accept-Language': lang,
            'Accept-Charset': charset
        }
    return {
        'Accept-Language': 'en-US',
        'Accept-Charset': 'utf-8'
    }

# Example Usage
ip = '8.8.8.8'  # Replace with the user's IP address
headers = get_default_headers(ip)
print(headers)
