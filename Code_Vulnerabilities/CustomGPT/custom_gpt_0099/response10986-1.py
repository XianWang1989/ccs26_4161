
import geoip2.database

def get_language_by_ip(ip_address):
    # Load the GeoIP2 database (download it from MaxMind)
    with geoip2.database.Reader('GeoLite2-Country.mmdb') as reader:
        try:
            # Get the country information from the IP address
            response = reader.country(ip_address)
            country_code = response.country.iso_code

            # Map country codes to Accept-Language and Accept-Charset
            language_map = {
                'US': ('en-US', 'utf-8'),
                'FR': ('fr-FR', 'iso-8859-1'),
                'DE': ('de-DE', 'iso-8859-1'),
                'RU': ('ru-RU', 'windows-1251'),
                'CN': ('zh-CN', 'gb2312'),
                # Add more country mappings as needed
            }
            # Get the default language and charset for the country
            return language_map.get(country_code, ('en-US', 'utf-8'))  # Default fallback

        except Exception as e:
            print(f"Error: {e}")
            return ('en-US', 'utf-8')  # Fallback in case of error

# Example usage
ip = '8.8.8.8'  # Example IP address
language, charset = get_language_by_ip(ip)
print(f"Default Accept-Language: {language}, Accept-Charset: {charset}")
