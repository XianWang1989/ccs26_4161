
import requests

# Predefined mapping of country codes to default Accept-Language and Accept-Charset headers
country_settings = {
    'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'UTF-8'},
    'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251'},
    'FR': {'Accept-Language': 'fr-FR,fr;q=0.9', 'Accept-Charset': 'UTF-8'},
    # Add more countries as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    if response.status_code == 200:
        data = response.json()
        return data.get('country', None)
    return None

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code and country_code in country_settings:
        return country_settings[country_code]
    return {'Accept-Language': 'en', 'Accept-Charset': 'UTF-8'}  # Default if country not found

# Example usage
ip_address = 'YOUR_IP_ADDRESS'  # Replace with the actual IP address
headers = get_default_headers(ip_address)
print(headers)
