
import requests

# Mapping of country codes to default language and charset
country_language_map = {
    'US': ('en-US', 'UTF-8'),
    'GB': ('en-GB', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    'FR': ('fr-FR', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    # Add more mappings as needed
}

def get_country_code(ip_address):
    """Get country code from IP address using a geolocation API."""
    response = requests.get(f'https://ipapi.co/{ip_address}/country/')
    return response.text.strip() if response.status_code == 200 else None

def get_default_headers(ip_address):
    """Determine default Accept-Language and Accept-Charset headers based on IP."""
    country_code = get_country_code(ip_address)

    if country_code in country_language_map:
        lang, charset = country_language_map[country_code]
        return {
            'Accept-Language': lang,
            'Accept-Charset': charset
        }
    else:
        # Default values if the country is not in the map
        return {
            'Accept-Language': 'en-US',
            'Accept-Charset': 'UTF-8'
        }

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP address
headers = get_default_headers(ip)
print(headers)
