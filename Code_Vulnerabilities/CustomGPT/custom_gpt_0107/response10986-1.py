
import geoip2.database

# Load the GeoIP database
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# Mapping of country codes to default Accept-Language and Accept-Charset
lang_charset_mapping = {
    'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'UTF-8'},
    'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251'},
    'DE': {'Accept-Language': 'de-DE,de;q=0.9', 'Accept-Charset': 'UTF-8'},
    # Add more country mappings as needed
}

def get_default_headers(ip):
    try:
        response = reader.city(ip)
        country_code = response.country.iso_code

        # Get the headers from the mapping
        if country_code in lang_charset_mapping:
            return lang_charset_mapping[country_code]
        else:
            return {'Accept-Language': 'en', 'Accept-Charset': 'UTF-8'}  # Default

    except Exception as e:
        print(f"Error: {e}")
        return {'Accept-Language': 'en', 'Accept-Charset': 'UTF-8'}  # Fallback

# Example usage
ip_address = '8.8.8.8'  # Replace with the actual IP address
headers = get_default_headers(ip_address)
print(headers)
