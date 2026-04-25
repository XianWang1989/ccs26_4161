
import geoip2.database

# Mapping of country codes to Accept-Language and Accept-Charset
country_language_map = {
    'US': ('en-US', 'utf-8'),
    'GB': ('en-GB', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'utf-8'),
    # Add more country codes and preferences as needed
}

def get_language_and_charset(ip_address):
    # Load GeoIP2 database (you need to download a GeoLite2 database)
    reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
    try:
        response = reader.country(ip_address)
        country_code = response.country.iso_code
        language, charset = country_language_map.get(country_code, ('en', 'utf-8'))
        return language, charset
    except Exception as e:
        print(f"Error: {e}")
        return 'en', 'utf-8'  # Default fallback

# Example usage
ip = '192.0.2.1'  # Replace with the client's IP address
language, charset = get_language_and_charset(ip)
print(f"Accept-Language: {language}, Accept-Charset: {charset}")
