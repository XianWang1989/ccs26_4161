
import requests
import geoip2.database

# Load GeoIP database (download from MaxMind)
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# Define language and charset mappings
country_language_mapping = {
    'US': {'language': 'en-US', 'charset': 'UTF-8'},
    'RU': {'language': 'ru-RU', 'charset': 'windows-1251'},
    'DE': {'language': 'de-DE', 'charset': 'UTF-8'},
    # Add more countries as needed
}

def get_country_code(ip):
    try:
        response = reader.country(ip)
        return response.country.iso_code
    except Exception as e:
        print(f"Error fetching country code: {e}")
        return None

def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in country_language_mapping:
        return country_language_mapping[country_code]
    else:
        return {'language': 'en', 'charset': 'UTF-8'}  # Default

# Example usage
ip_address = '8.8.8.8'  # Replace with user's IP
headers = get_default_headers(ip_address)
print(f"Default headers for {ip_address}: {headers}")
