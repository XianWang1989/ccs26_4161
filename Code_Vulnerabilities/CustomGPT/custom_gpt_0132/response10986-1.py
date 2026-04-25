
import requests
import geoip2.database

# Load GeoLite2 Database
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

def get_country_code(ip):
    try:
        response = reader.city(ip)
        return response.country.iso_code  # Returns country code (e.g., 'US', 'RU')
    except Exception as e:
        print(f"Error resolving IP: {e}")
        return None

def get_default_language_and_charset(country_code):
    # Map country codes to default Accept-Language and Accept-Charset
    country_map = {
        'US': ('en-US', 'utf-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'FR': ('fr-FR', 'utf-8'),
        # Add more mappings as needed
    }

    return country_map.get(country_code, ('en', 'utf-8'))  # Default to English/UTF-8

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
country_code = get_country_code(ip_address)

if country_code:
    language, charset = get_default_language_and_charset(country_code)
    print(f"Default Accept-Language: {language}")
    print(f"Default Accept-Charset: {charset}")
