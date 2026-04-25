
import requests

def get_country_code(ip_address):
    # Use a geo-IP service to get the country code from IP
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    response_data = response.json()
    return response_data.get('countryCode')

def get_default_accept_language(country_code):
    # Dictionary mapping country codes to default Accept-Language headers
    language_mapping = {
        'US': 'en-US,en;q=0.9',
        'DE': 'de-DE,de;q=0.9',
        'FR': 'fr-FR,fr;q=0.9',
        'RU': 'ru-RU,ru;q=0.9',
        'ES': 'es-ES,es;q=0.9',
        # Add more mappings as needed
    }
    return language_mapping.get(country_code, 'en')

def determine_accept_language(ip_address):
    country_code = get_country_code(ip_address)
    accept_language = get_default_accept_language(country_code)
    return accept_language

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP
header_value = determine_accept_language(ip_address)
print(f'Default Accept-Language for {ip_address}: {header_value}')
