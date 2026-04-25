
import requests
import geoip2.database

# Load the GeoLite2 database
reader = geoip2.database.Reader('/path/to/GeoLite2-Country.mmdb')

# Function to get the default Accept-Language based on IP
def get_accept_language(ip_address):
    try:
        # Get country code using GeoIP
        response = reader.country(ip_address)
        country_code = response.country.iso_code

        # Map country codes to default Accept-Language
        language_mapping = {
            'US': 'en-US',
            'RU': 'ru-RU',
            'FR': 'fr-FR',
            'DE': 'de-DE',
            'CN': 'zh-CN',
            # Add more mappings as needed
        }

        return language_mapping.get(country_code, 'en-US')  # Default to en-US
    except Exception as e:
        print(f"Error: {e}")
        return 'en-US'  # Fallback

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
default_language = get_accept_language(ip_address)
print(f'Default Accept-Language for IP {ip_address}: {default_language}')
