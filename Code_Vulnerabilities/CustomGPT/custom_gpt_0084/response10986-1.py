
import requests

# Example mapping of country codes to default Accept-Language and character set
country_language_map = {
    'US': ('en-US', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    # Add more mappings as needed
}

def get_country_code(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        data = response.json()
        return data.get('country')  # Returns country code
    except Exception as e:
        print(f"Error fetching country code: {e}")
        return None

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code and country_code in country_language_map:
        language, charset = country_language_map[country_code]
        return {
            'Accept-Language': language,
            'Accept-Charset': charset
        }
    return None

# Example usage:
ip_address = '8.8.8.8'  # Replace with the actual IP address
headers = get_default_headers(ip_address)
if headers:
    print(headers)
else:
    print("Could not determine headers.")
