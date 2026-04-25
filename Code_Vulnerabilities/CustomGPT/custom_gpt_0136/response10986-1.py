
import requests
import geoip2.database

# Function to get the country code from an IP address
def get_country_code(ip_address):
    # Load GeoIP2 database (you need to download the database file)
    reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
    response = reader.country(ip_address)
    return response.country.iso_code

# Function to determine default Accept-Language based on country code
def get_default_accept_language(country_code):
    language_mapping = {
        'US': 'en-US',
        'GB': 'en-GB',
        'FR': 'fr-FR',
        'DE': 'de-DE',
        'RU': 'ru-RU',
        # Add more country codes and their default languages here
    }
    return language_mapping.get(country_code, 'en')

# Example usage
ip_address = '8.8.8.8'  # Example IP
country_code = get_country_code(ip_address)
default_language = get_default_accept_language(country_code)

print(f'Default Accept-Language for IP {ip_address} is: {default_language}')
