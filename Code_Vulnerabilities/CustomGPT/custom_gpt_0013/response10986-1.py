
import requests

# Mapping of country codes to Accept-Language and Accept-Charset
country_language_map = {
    'US': ('en-US', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'utf-8'),
    'DE': ('de-DE', 'utf-8'),
    'JP': ('ja-JP', 'utf-8'),
    # Add more countries as needed
}

def get_country_from_ip(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        data = response.json()
        return data.get('country', '').upper()
    except Exception as e:
        print(f"Error fetching country from IP: {e}")
        return None

def get_default_headers(ip):
    country_code = get_country_from_ip(ip)
    if country_code:
        return country_language_map.get(country_code, ('en-US', 'utf-8'))  # Default if not found
    return ('en-US', 'utf-8')  # Fallback defaults

# Example usage
ip_address = '8.8.8.8'  # Example IP address
language, charset = get_default_headers(ip_address)
print(f"Default Accept-Language: {language}, Accept-Charset: {charset}")
