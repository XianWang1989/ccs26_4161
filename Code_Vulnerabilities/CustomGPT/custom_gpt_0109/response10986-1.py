
import geoip2.database

# Load the GeoIP2 database
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# Define a mapping of country codes to default Accept-Language headers
country_lang_map = {
    'US': 'en-US',
    'FR': 'fr-FR',
    'DE': 'de-DE',
    'RU': 'ru-RU',
    # Add more mappings as necessary
}

def get_language_from_ip(ip):
    try:
        response = reader.country(ip)
        country_code = response.country.iso_code
        return country_lang_map.get(country_code, 'en')  # Default to English if not found
    except Exception as e:
        print(f"Error: {e}")
        return 'en'  # Default to English on error

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP
lang_header = get_language_from_ip(ip_address)
print(f'Default Accept-Language for IP {ip_address} is: {lang_header}')
