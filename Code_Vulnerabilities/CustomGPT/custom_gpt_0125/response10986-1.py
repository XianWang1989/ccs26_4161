
import requests

# Mapping of country codes to preferred Accept-Language headers
COUNTRY_LANGUAGES = {
    'US': 'en-US,en;q=0.9',
    'GB': 'en-GB,en;q=0.9',
    'FR': 'fr-FR,fr;q=0.9',
    'DE': 'de-DE,de;q=0.9',
    'RU': 'ru-RU,ru;q=0.9',
    # Add more country codes and languages as needed
}

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    if response.status_code == 200:
        return response.json().get('country', 'US')  # Default to US if unknown
    return 'US'

def get_accept_language(ip):
    country_code = get_country_code(ip)
    return COUNTRY_LANGUAGES.get(country_code, 'en-US,en;q=0.9')  # Default if not found

# Example usage
user_ip = '8.8.8.8'  # Replace with the user's IP address
accept_language = get_accept_language(user_ip)
print(f'The default Accept-Language for IP {user_ip} is: {accept_language}')
