
import requests
from countryinfo import CountryInfo

# Function to get the country code from an IP address
def get_country_code(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        response_data = response.json()
        return response_data.get('country')
    except Exception as e:
        print(f"Error fetching country code: {e}")
        return None

# Function to get the default Accept-Language header for a given country code
def get_default_accept_language(country_code):
    # Mapping of country codes to common Accept-Language values
    language_map = {
        'US': 'en-US,en;q=0.9',
        'CA': 'en-CA,fr-CA;q=0.8',
        'FR': 'fr-FR,fr;q=0.9',
        'DE': 'de-DE,de;q=0.9',
        'RU': 'ru-RU,ru;q=0.9',
        'JP': 'ja-JP,ja;q=0.9',
        # Add more mappings as needed
    }
    return language_map.get(country_code, 'en-US')  # Default to English if the country is not in the map

# Example usage
ip_address = '8.8.8.8'  # Replace this with the actual IP address
country_code = get_country_code(ip_address)

if country_code:
    default_language = get_default_accept_language(country_code)
    print(f"Default Accept-Language for IP {ip_address} (Country Code: {country_code}): {default_language}")
else:
    print("Could not determine country code.")
