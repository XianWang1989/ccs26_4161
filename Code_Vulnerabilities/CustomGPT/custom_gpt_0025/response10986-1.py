
import requests

# Mapping of country codes to Accept-Language and Accept-Charset
COUNTRY_LANG_CHARSET_MAP = {
    'US': ('en-US', 'utf-8'),
    'GB': ('en-GB', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'DE': ('de-DE', 'utf-8'),
    # Add more mappings as needed
}

def get_country_code(ip_address):
    """Get the country code from IP address using a geolocation service."""
    response = requests.get(f'https://ipapi.co/{ip_address}/country/')
    return response.text.strip()

def get_default_headers(ip_address):
    """Determine default headers based on IP address."""
    country_code = get_country_code(ip_address)
    return COUNTRY_LANG_CHARSET_MAP.get(country_code, ('en-US', 'utf-8'))

# Example usage
ip = '8.8.8.8'  # Example IP address (Google Public DNS)
language, charset = get_default_headers(ip)
print(f'Default Accept-Language: {language}')
print(f'Default Accept-Charset: {charset}')
