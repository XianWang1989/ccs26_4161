
import requests
import geoip2.database

# Load the GeoLite2 database for IP geolocation
geolite2_db = geoip2.database.Reader('path/to/GeoLite2-Country.mmdb')

# Define a mapping of country codes to default Accept-Language and Accept-Charset
country_defaults = {
    'US': ('en-US', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    # Add more country codes as needed
}

def get_country_from_ip(ip_address):
    try:
        response = geolite2_db.country(ip_address)
        return response.country.iso_code
    except Exception as e:
        print(f"Error fetching data for IP {ip_address}: {e}")
        return None

def get_default_language_and_charset(ip_address):
    country_code = get_country_from_ip(ip_address)
    if country_code and country_code in country_defaults:
        return country_defaults[country_code]
    else:
        return ('en', 'UTF-8')  # Fallback to default

# Example usage
ip_address = '8.8.8.8'  # Replace with any IP address
language, charset = get_default_language_and_charset(ip_address)
print(f"Default Accept-Language: {language}, Accept-Charset: {charset}")
