
import requests

# Dictionary of common Accept-Language headers by country code
country_language_map = {
    'US': 'en-US,en;q=0.9',
    'FR': 'fr-FR,fr;q=0.9',
    'DE': 'de-DE,de;q=0.9',
    'RU': 'ru-RU,ru;q=0.9',
    'CN': 'zh-CN,zh;q=0.9',
    # Add other countries as needed
}

def get_country_code(ip_address):
    """Fetch the country code from the IP address using a geolocation API."""
    response = requests.get(f'https://ipapi.co/{ip_address}/country/')
    return response.text.strip()

def get_default_accept_language(ip_address):
    """Determine the default Accept-Language header based on IP address."""
    country_code = get_country_code(ip_address)
    return country_language_map.get(country_code, 'en-US,en;q=0.9')  # Fallback to a default

# Example usage
ip = '8.8.8.8'  # Replace with the target IP address
language_header = get_default_accept_language(ip)
print(f'Default Accept-Language for IP {ip}: {language_header}')
