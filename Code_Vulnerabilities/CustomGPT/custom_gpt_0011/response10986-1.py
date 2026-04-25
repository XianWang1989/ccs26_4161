
import requests

# Mapping of country codes to default Accept-Language and Accept-Charset
COUNTRY_LANGUAGES = {
    'US': ('en-US', 'UTF-8'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'CN': ('zh-CN', 'UTF-8'),
    # Add more country mappings as needed
}

def get_country_code(ip_address):
    """Fetch the country code based on the IP address."""
    response = requests.get(f'https://ipapi.co/{ip_address}/country/')
    return response.text.strip()

def get_default_accept_headers(ip_address):
    """Retrieve the default Accept-Language and Accept-Charset based on IP address."""
    country_code = get_country_code(ip_address)
    language, charset = COUNTRY_LANGUAGES.get(country_code, ('en-US', 'UTF-8'))  # Default to US

    return {'Accept-Language': language, 'Accept-Charset': charset}

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP address
headers = get_default_accept_headers(ip)
print(headers)  # {'Accept-Language': 'en-US', 'Accept-Charset': 'UTF-8'}
