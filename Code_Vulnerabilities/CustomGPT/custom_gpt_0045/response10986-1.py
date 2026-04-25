
import requests

def get_country_code(ip_address):
    # Use an IP geolocation service to get the country code
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    return data.get('country', None)

def default_accept_language(country_code):
    # Mapping of country codes to default Accept-Language headers
    language_map = {
        'US': 'en-US,en;q=0.9',
        'GB': 'en-GB,en;q=0.9',
        'FR': 'fr-FR,fr;q=0.9',
        'DE': 'de-DE,de;q=0.9',
        'RU': 'ru-RU,ru;q=0.9',
        'IT': 'it-IT,it;q=0.9',
        # Add more country codes and languages as needed
    }
    return language_map.get(country_code, 'en-US,en;q=0.9')  # default to English if country not found

def get_default_accept_language(ip_address):
    country_code = get_country_code(ip_address)
    if country_code:
        return default_accept_language(country_code)
    return None

# Example usage
ip = '8.8.8.8'  # Example IP address
accept_language = get_default_accept_language(ip)
print(f"The default Accept-Language header for IP {ip} is: {accept_language}")
