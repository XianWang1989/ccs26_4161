
import requests

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    return response.json().get('country')

def get_default_language(country_code):
    language_map = {
        'US': 'en-US',
        'FR': 'fr-FR',
        'DE': 'de-DE',
        'RU': 'ru-RU',
        'CN': 'zh-CN',
        # Add more country codes and languages as needed
    }
    return language_map.get(country_code, 'en-US')  # Default to English

def main(ip):
    country_code = get_country_code(ip)
    default_language = get_default_language(country_code)
    print(f'Default Accept-Language for {country_code}: {default_language}')

# Example IP address
main('8.8.8.8')  # Replace with the target IP address
