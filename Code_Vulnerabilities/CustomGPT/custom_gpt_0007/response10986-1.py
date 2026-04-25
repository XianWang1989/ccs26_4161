
import requests

# Mapping of country codes to their default Accept-Language
country_languages = {
    'US': 'en-US,en;q=0.5',
    'GB': 'en-GB,en;q=0.5',
    'DE': 'de-DE,de;q=0.5',
    'FR': 'fr-FR,fr;q=0.5',
    'RU': 'ru-RU,ru;q=0.5',
    # Add more mappings as needed
}

def get_country_code(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        return response.get('country', None)
    except Exception as e:
        print(f"Error fetching country code: {e}")
        return None

def get_accept_language(ip_address):
    country_code = get_country_code(ip_address)
    if country_code:
        return country_languages.get(country_code, 'en')  # Default to 'en' if not found
    return None

# Example usage
ip_address = '8.8.8.8'  # Sample IP address
accept_language = get_accept_language(ip_address)
print(f"Default Accept-Language for {ip_address}: {accept_language}")
