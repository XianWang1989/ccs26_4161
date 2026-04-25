
import requests

# A simple mapping of country codes to default Accept-Language headers
country_language_map = {
    'US': 'en-US,en;q=0.9',
    'FR': 'fr-FR,fr;q=0.9',
    'DE': 'de-DE,de;q=0.9',
    'RU': 'ru-RU,ru;q=0.9',
    'CN': 'zh-CN,zh;q=0.9',
    # Add more country codes and languages as needed
}

def get_country_code(ip_address):
    """Get country code from IP address using an external API."""
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    if response.status_code == 200:
        return response.json().get('country')
    return None

def get_default_accept_language(ip_address):
    """Determine the default Accept-Language header based on the IP address."""
    country_code = get_country_code(ip_address)
    if country_code in country_language_map:
        return country_language_map[country_code]
    return 'en-US'  # Fallback to English if country code not found

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
accept_language = get_default_accept_language(ip_address)
print(f"Default Accept-Language for IP {ip_address}: {accept_language}")
