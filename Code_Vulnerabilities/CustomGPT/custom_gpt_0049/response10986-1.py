
import requests

# Example mapping of country codes to language and charset
language_mapping = {
    'US': {'language': 'en-US', 'charset': 'UTF-8'},
    'RU': {'language': 'ru-RU', 'charset': 'windows-1251'},
    'DE': {'language': 'de-DE', 'charset': 'UTF-8'},
    'FR': {'language': 'fr-FR', 'charset': 'UTF-8'},
    # Add more mappings as needed
}

def get_language_by_ip(ip_address):
    # Get country code from IP address using a geolocation API
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()

    if data['status'] == 'fail':
        return None  # Return None if there's an issue with the request

    country_code = data['countryCode']

    # Lookup language and charset based on country code
    if country_code in language_mapping:
        return language_mapping[country_code]
    else:
        return {'language': 'en', 'charset': 'UTF-8'}  # Default values if country not found

# Example usage
ip_address = '8.8.8.8'  # Replace with actual IP address
result = get_language_by_ip(ip_address)
if result:
    print(f"Default Accept-Language: {result['language']}, Accept-Charset: {result['charset']}")
else:
    print("Could not determine language and charset.")
