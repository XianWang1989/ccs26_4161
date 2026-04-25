
import requests

def get_country_by_ip(ip_address):
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    data = response.json()
    return data.get('countryCode')

def get_default_language_by_country(country_code):
    country_languages = {
        'US': 'en-US',
        'FR': 'fr-FR',
        'DE': 'de-DE',
        'RU': 'ru-RU',
        # Add more mappings as needed
    }
    return country_languages.get(country_code, 'en')  # Default to English if not found

ip_address = '8.8.8.8'  # Example IP
country_code = get_country_by_ip(ip_address)
default_language = get_default_language_by_country(country_code)

print(f"The default Accept-Language for IP {ip_address} is: {default_language}")
