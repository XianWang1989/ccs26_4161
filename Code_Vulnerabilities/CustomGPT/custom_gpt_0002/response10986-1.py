
import geoip2.database

# Load GeoLite2 database
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

def get_language_by_ip(ip):
    try:
        response = reader.country(ip)
        country_code = response.country.iso_code
        return map_country_to_language(country_code)
    except Exception as e:
        print(f"Error: {e}")
        return None

def map_country_to_language(country_code):
    country_language_map = {
        'US': ('en-US', 'UTF-8'),
        'FR': ('fr-FR', 'UTF-8'),
        'DE': ('de-DE', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        # Add more countries and their common languages/charsets here
    }
    return country_language_map.get(country_code, ('en', 'UTF-8'))

# Example usage
ip_address = '128.101.101.101'  # Replace with the user's IP
language, charset = get_language_by_ip(ip_address)
print(f"Default Accept-Language: {language}, Accept-Charset: {charset}")
