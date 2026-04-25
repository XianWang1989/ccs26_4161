
import requests

# Mapping of country codes to default Accept-Language and Accept-Charset
country_language_mapping = {
    'US': ('en-US', 'utf-8'),
    'FR': ('fr-FR', 'iso-8859-1'),
    'DE': ('de-DE', 'iso-8859-1'),
    'RU': ('ru-RU', 'windows-1251'),
    'CN': ('zh-CN', 'utf-8'),
    # Add more country codes and mappings as needed
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
    if country_code and country_code in country_language_mapping:
        language, charset = country_language_mapping[country_code]
        return {
            'Accept-Language': language,
            'Accept-Charset': charset,
        }
    else:
        return {
            'Accept-Language': 'en-US',
            'Accept-Charset': 'utf-8',  # Fallback
        }

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP address
headers = get_default_headers(ip)
print(headers)
