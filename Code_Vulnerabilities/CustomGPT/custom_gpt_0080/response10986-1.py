
import geoip2.database

# Load the GeoIP database
reader = geoip2.database.Reader('path/to/GeoLite2-Country.mmdb')

# Mapping of country codes to default Accept-Language and Accept-Charset
country_mapping = {
    'US': ('en-US', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    'CN': ('zh-CN', 'UTF-8'),
    # Add more countries as needed
}

def get_accept_headers(ip):
    try:
        response = reader.country(ip)
        country_code = response.country.iso_code

        if country_code in country_mapping:
            return country_mapping[country_code]
        else:
            return ('en-US', 'UTF-8')  # Default values if country not found

    except Exception as e:
        print(f"Error fetching data: {e}")
        return ('en-US', 'UTF-8')  # Fallback

# Example usage
ip_address = '8.8.8.8'  # Replace with user's IP
language, charset = get_accept_headers(ip_address)
print(f"Accept-Language: {language}, Accept-Charset: {charset}")
