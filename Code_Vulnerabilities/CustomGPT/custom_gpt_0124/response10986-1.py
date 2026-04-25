
import requests

# Mapping of country codes to default Accept-Language and Accept-Charset headers
country_language_map = {
    'US': ('en-US', 'UTF-8'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    # Add more countries as needed
}

def get_country_code(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        data = response.json()
        return data.get('country')
    except Exception as e:
        print(f"Error retrieving country code: {e}")
        return None

def determine_headers(ip_address):
    country_code = get_country_code(ip_address)

    if country_code in country_language_map:
        language, charset = country_language_map[country_code]
        return language, charset
    else:
        return 'en', 'UTF-8'  # Default values if country not found

# Example usage
ip_address = '8.8.8.8'  # Replace with an actual IP address
language, charset = determine_headers(ip_address)
print(f"Default Accept-Language: {language}, Accept-Charset: {charset}")
