
import requests

# Function to get country code from IP
def get_country_from_ip(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    return response.json().get('country')

# Dictionary mapping of country codes to default Accept-Language and Accept-Charset
default_headers = {
    'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'UTF-8'},
    'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251'},
    'FR': {'Accept-Language': 'fr-FR,fr;q=0.9', 'Accept-Charset': 'ISO-8859-1'},
    # Add more countries as needed...
}

def get_default_headers(ip):
    country_code = get_country_from_ip(ip)
    return default_headers.get(country_code, {'Accept-Language': 'en', 'Accept-Charset': 'UTF-8'})

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
default_accept_headers = get_default_headers(ip_address)
print(default_accept_headers)
