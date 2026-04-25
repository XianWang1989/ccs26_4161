
import requests

# Function to get country code from IP
def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    return data.get('country')

# Mapping of country codes to default Accept-Language headers
language_map = {
    'US': 'en-US,en;q=0.5',
    'GB': 'en-GB,en;q=0.5',
    'DE': 'de-DE,de;q=0.5',
    'FR': 'fr-FR,fr;q=0.5',
    'RU': 'ru-RU,ru;q=0.5',
    # Add more mappings as needed
}

# Function to get default Accept-Language for a country
def get_default_accept_language(ip_address):
    country_code = get_country_code(ip_address)
    if country_code in language_map:
        return language_map[country_code]
    else:
        return 'en;q=0.5'  # Default to English if country not mapped

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP address
accept_language = get_default_accept_language(ip)
print(f"Default Accept-Language for IP {ip}: {accept_language}")
