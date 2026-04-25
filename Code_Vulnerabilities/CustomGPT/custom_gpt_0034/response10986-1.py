
import requests

# Example function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/country/')
    if response.status_code == 200:
        return response.text
    return None

# Mapping of country codes to default Accept-Language and Accept-Charset
country_language_map = {
    'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'UTF-8'},
    'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251'},
    'FR': {'Accept-Language': 'fr-FR,fr;q=0.9', 'Accept-Charset': 'UTF-8'},
    # Add more mappings as needed
}

def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in country_language_map:
        return country_language_map[country_code]
    return {'Accept-Language': 'en', 'Accept-Charset': 'UTF-8'}  # Fallback headers

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
default_headers = get_default_headers(ip_address)
print(default_headers)
