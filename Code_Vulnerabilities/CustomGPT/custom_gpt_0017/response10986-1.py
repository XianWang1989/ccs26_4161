
import geoip2.database

# Load the GeoIP2 database
reader = geoip2.database.Reader('path/to/GeoLite2-Country.mmdb')

# Define a mapping of country codes to default Accept-Language and Accept-Charset
country_languages = {
    'US': ('en-US', 'utf-8'),
    'FR': ('fr-FR', 'iso-8859-1'),
    'DE': ('de-DE', 'iso-8859-1'),
    'RU': ('ru-RU', 'windows-1251'),
    # Add more countries as needed
}

def get_default_language_and_charset(ip_address):
    try:
        response = reader.city(ip_address)
        country_code = response.country.iso_code
        return country_languages.get(country_code, ('en-US', 'utf-8'))  # Default to en-US, utf-8
    except Exception as e:
        print(f"Error: {e}")
        return ('en-US', 'utf-8')  # Fallback

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP address
language, charset = get_default_language_and_charset(ip)
print(f"Default Accept-Language: {language}, Accept-Charset: {charset}")
