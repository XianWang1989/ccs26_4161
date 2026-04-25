
import geoip2.database

# Load the GeoLite2 database
reader = geoip2.database.Reader('path_to_your/GeoLite2-Country.mmdb')

# Mapping of country codes to popular accept language and charset values
country_language_map = {
    'US': {'language': 'en-US', 'charset': 'UTF-8'},
    'FR': {'language': 'fr-FR', 'charset': 'ISO-8859-1'},
    'DE': {'language': 'de-DE', 'charset': 'UTF-8'},
    'RU': {'language': 'ru-RU', 'charset': 'windows-1251'},
    # Add more countries as needed
}

def get_language_and_charset(ip_address):
    try:
        # Get the country from the IP address
        response = reader.country(ip_address)
        country_code = response.country.iso_code

        # Get the default language and charset based on the country code
        return country_language_map.get(country_code, {'language': 'en', 'charset': 'UTF-8'})

    except Exception as e:
        print(f"Error: {e}")
        return {'language': 'en', 'charset': 'UTF-8'}

# Example usage
ip_address = '128.101.101.101'  # Replace with the user's IP address
default_language_and_charset = get_language_and_charset(ip_address)

print(f"Accept-Language: {default_language_and_charset['language']}")
print(f"Accept-Charset: {default_language_and_charset['charset']}")
