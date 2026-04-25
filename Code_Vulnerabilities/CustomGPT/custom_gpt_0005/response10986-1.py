
import requests
import geoip2.database

# Load GeoIP database
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

def get_language_by_ip(ip):
    # Get country code from IP
    try:
        response = reader.country(ip)
        country_code = response.country.iso_code
    except Exception as e:
        return f"Error: {e}"

    # Map country codes to common Accept-Language headers
    language_map = {
        'US': 'en-US',
        'GB': 'en-GB',
        'FR': 'fr-FR',
        'DE': 'de-DE',
        'JP': 'ja-JP',
        # Add more country mappings as needed
    }

    return language_map.get(country_code, 'en-US')  # Default to en-US if not found

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
language = get_language_by_ip(ip_address)
print(f"Default Accept-Language for {ip_address}: {language}")
