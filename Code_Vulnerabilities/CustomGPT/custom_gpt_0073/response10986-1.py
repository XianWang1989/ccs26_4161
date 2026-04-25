
import requests

def get_country_code(ip_address):
    response = requests.get(f"https://ipapi.co/{ip_address}/json/")
    data = response.json()
    return data.get('country', '')

def get_default_language_and_charset(country_code):
    language_map = {
        'US': ('en-US', 'UTF-8'),
        'FR': ('fr-FR', 'UTF-8'),
        'DE': ('de-DE', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        # Add more mappings as needed
    }
    return language_map.get(country_code, ('en-US', 'UTF-8'))  # Default fallback

# Example usage
ip = "8.8.8.8"  # Example IP address
country_code = get_country_code(ip)
language, charset = get_default_language_and_charset(country_code)

print(f"Country Code: {country_code}, Default Language: {language}, Default Charset: {charset}")
