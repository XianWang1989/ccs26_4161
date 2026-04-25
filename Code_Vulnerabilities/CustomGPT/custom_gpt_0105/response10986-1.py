
import geoip2.database

# Load your GeoIP2 database (download one from MaxMind)
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# Function to get default language and charset based on IP
def get_default_language_and_charset(ip_address):
    try:
        response = reader.country(ip_address)
        country_code = response.country.iso_code

        # Define your mappings here
        language_mapping = {
            'US': ('en-US', 'utf-8'),
            'RU': ('ru-RU', 'windows-1251'),
            'FR': ('fr-FR', 'utf-8'),
            'DE': ('de-DE', 'utf-8'),
            'CN': ('zh-CN', 'utf-8'),
            # Add more mappings as needed
        }

        # Get default language and charset
        return language_mapping.get(country_code, ('en-US', 'utf-8'))  # Default to English if not found

    except geoip2.errors.GeoIP2Error:
        return ('en-US', 'utf-8')  # Default on error

# Example usage
ip_address = '128.101.101.101'  # Replace with the actual IP you want to check
language, charset = get_default_language_and_charset(ip_address)
print(f'Default Accept-Language: {language}, Accept-Charset: {charset}')

# Close the GeoIP2 reader
reader.close()
