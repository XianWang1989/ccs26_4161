
import requests

# Mapping of country codes to common Accept-Language values
country_language_map = {
    'US': 'en-US,en;q=0.9',
    'GB': 'en-GB,en;q=0.9',
    'DE': 'de-DE,de;q=0.9',
    'FR': 'fr-FR,fr;q=0.9',
    'RU': 'ru-RU,ru;q=0.9',
    # Add more mappings as needed
}

def get_country_code(ip_address):
    """Get the country code from the IP address using a geolocation API."""
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        data = response.json()
        return data.get('country')
    except Exception as e:
        print(f"Error retrieving country code: {e}")
        return None

def get_default_accept_language(ip_address):
    """Determine the default Accept-Language based on IP address."""
    country_code = get_country_code(ip_address)
    if country_code:
        return country_language_map.get(country_code, 'en')
    return 'en'  # Default to English if country code is not found

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
accept_language = get_default_accept_language(ip_address)
print(f"Default Accept-Language for IP {ip_address}: {accept_language}")
