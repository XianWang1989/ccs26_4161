
import requests

# Function to get country code from IP address
def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/country/')
    if response.status_code == 200:
        return response.text  # Returns country code (e.g., "US", "RU")
    return None

# Map of country codes to default Accept-Language headers
country_language_map = {
    'US': 'en-US,en;q=0.9',
    'RU': 'ru-RU,ru;q=0.9',
    'DE': 'de-DE,de;q=0.9',
    'FR': 'fr-FR,fr;q=0.9',
    # Add more countries as needed
}

# Function to get default Accept-Language based on IP
def get_default_accept_language(ip_address):
    country_code = get_country_code(ip_address)
    if country_code:
        return country_language_map.get(country_code, 'en-US,en;q=0.9')  # Default to English if not found
    return None

# Example usage
ip_address = '8.8.8.8'  # Replace with actual IP
default_language = get_default_accept_language(ip_address)
print(f'Default Accept-Language for IP {ip_address}: {default_language}')
