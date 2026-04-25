
import requests

def get_country_code(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data.get("country")

def get_default_language_charset(country_code):
    # Mapping of country codes to language and charset
    language_charset_mapping = {
        'US': ('en-US', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'FR': ('fr-FR', 'UTF-8'),
        'DE': ('de-DE', 'UTF-8'),
        # Add more mappings as needed
    }
    return language_charset_mapping.get(country_code, ('en', 'UTF-8'))

def determine_headers(ip):
    country_code = get_country_code(ip)
    language, charset = get_default_language_charset(country_code)
    return {
        'Accept-Language': language,
        'Accept-Charset': charset
    }

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP
headers = determine_headers(ip_address)
print(headers)
