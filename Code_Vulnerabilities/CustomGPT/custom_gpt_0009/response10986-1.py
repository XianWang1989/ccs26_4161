
import requests

# Example function to get country code from IP
def get_country_code(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = response.json()
    return data.get('country')

# Function to determine default Accept-Language based on country code
def detect_accept_language(country_code):
    # Mapping of country codes to default Accept-Language values
    language_map = {
        'US': 'en-US,en;q=0.9',
        'GB': 'en-GB,en;q=0.9',
        'FR': 'fr-FR,fr;q=0.9',
        'DE': 'de-DE,de;q=0.9',
        'RU': 'ru-RU,ru;q=0.9',
        # Add more country codes as needed
    }
    return language_map.get(country_code, 'en')  # Default to English if not found

# Example usage
ip_address = 'YOUR_IP_ADDRESS_HERE'  # Replace with the actual IP address
country_code = get_country_code(ip_address)
accept_language = detect_accept_language(country_code)

print(f'The default Accept-Language for IP {ip_address} (Country: {country_code}) is: {accept_language}')
