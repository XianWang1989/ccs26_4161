
import geoip2.database

# Sample country to Accept-Language mapping
country_language_map = {
    'US': 'en-US,en;q=0.9',
    'FR': 'fr-FR,fr;q=0.9',
    'DE': 'de-DE,de;q=0.9',
    'RU': 'ru-RU,ru;q=0.9',
    # Add more mappings as needed
}

def get_accept_language(ip_address):
    # Load the GeoIP database
    reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

    try:
        response = reader.country(ip_address)
        country_code = response.country.iso_code
        accept_language = country_language_map.get(country_code, 'en-US')
        return accept_language
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return 'en-US'  # Default fallback

# Example usage
ip = '8.8.8.8'  # Example IP address
accept_language_header = get_accept_language(ip)
print(f'Default Accept-Language for {ip}: {accept_language_header}')
