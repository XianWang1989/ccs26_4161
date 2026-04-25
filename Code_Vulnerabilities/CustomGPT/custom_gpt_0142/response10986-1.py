
import requests
import geoip2.database

# Load the GeoIP database
geoip_reader = geoip2.database.Reader('path/to/GeoLite2-Country.mmdb')

def get_country_code(ip_address):
    try:
        response = geoip_reader.country(ip_address)
        return response.country.iso_code
    except Exception as e:
        print(f"Error retrieving country code: {e}")
        return None

def default_accept_headers(country_code):
    language_map = {
        'US': ('en-US', 'UTF-8'),
        'DE': ('de-DE', 'UTF-8'),
        'FR': ('fr-FR', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        # Add more country codes and their corresponding headers
    }
    return language_map.get(country_code, ('en', 'UTF-8'))  # Default to English

# Example Usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
country_code = get_country_code(ip_address)

if country_code:
    accept_language, accept_charset = default_accept_headers(country_code)
    print(f"Country Code: {country_code}")
    print(f"Default Accept-Language: {accept_language}")
    print(f"Default Accept-Charset: {accept_charset}")
else:
    print("Could not determine country code.")
