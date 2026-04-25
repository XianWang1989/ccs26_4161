
import requests
import geoip2.database

# Function to get country code from IP address
def get_country_code(ip_address):
    with geoip2.database.Reader('path/to/GeoLite2-Country.mmdb') as reader:
        response = reader.city(ip_address)
        return response.country.iso_code

# Function to determine default Accept-Language based on country code
def get_default_language(country_code):
    language_map = {
        'US': 'en-US',
        'GB': 'en-GB',
        'FR': 'fr-FR',
        'DE': 'de-DE',
        'RU': 'ru-RU',
        # Add more country-code => language mappings as needed
    }
    return language_map.get(country_code, 'en-US')  # Default to English if not found

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP
country_code = get_country_code(ip_address)
default_language = get_default_language(country_code)

print(f"IP: {ip_address}, Country Code: {country_code}, Default Accept-Language: {default_language}")
