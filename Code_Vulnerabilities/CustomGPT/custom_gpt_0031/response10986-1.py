
import requests

# Create a mapping of country codes to common Accept-Language and Accept-Charset headers
country_language_map = {
    'US': ('en-US,en;q=0.5', 'utf-8'),
    'RU': ('ru-RU,ru;q=0.9', 'windows-1251'),
    'FR': ('fr-FR,fr;q=0.9', 'utf-8'),
    'DE': ('de-DE,de;q=0.9', 'utf-8'),
    # Add more country codes and preferences as needed
}

def get_country_code(ip_address):
    # Use a geolocation service to get the country code
    response = requests.get(f'https://ipapi.co/{ip_address}/country/')
    if response.ok:
        return response.text.strip()
    return None

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)

    if country_code in country_language_map:
        return country_language_map[country_code]

    # Return defaults if the country code isn't in the map
    return ('en-US,en;q=0.5', 'utf-8')  # default to US preferences

# Example usage
ip_address = '8.8.8.8'  # Replace with actual IP to test
language, charset = get_default_headers(ip_address)
print(f'Default Accept-Language: {language}')
print(f'Default Accept-Charset: {charset}')
