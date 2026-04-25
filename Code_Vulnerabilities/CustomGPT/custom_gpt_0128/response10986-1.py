
import requests

# A mapping of country codes to default Accept-Language and Accept-Charset
country_language_mapping = {
    'US': ('en-US', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'utf-8'),
    'DE': ('de-DE', 'utf-8'),
    # Add more country mappings as needed
}

def get_country(ip_address):
    """Fetch the country code based on the IP address."""
    response = requests.get(f'https://ipapi.co/{ip_address}/country/')
    return response.text.strip()

def get_default_headers(ip_address):
    """Determine default Accept-Language and Accept-Charset based on IP."""
    country_code = get_country(ip_address)
    if country_code in country_language_mapping:
        return country_language_mapping[country_code]
    else:
        return ('en-US', 'utf-8')  # Default to English if country not mapped

# Example usage
ip_address = '8.8.8.8'  # Replace with the IP address to check
accept_language, accept_charset = get_default_headers(ip_address)

print(f'Accept-Language: {accept_language}')
print(f'Accept-Charset: {accept_charset}')
