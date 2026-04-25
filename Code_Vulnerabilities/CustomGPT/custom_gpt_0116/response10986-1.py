
import requests

def get_country_code(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data.get('country')

def get_default_language(country_code):
    language_map = {
        'US': 'en-US',
        'FR': 'fr-FR',
        'DE': 'de-DE',
        'RU': 'ru-RU',
        'JP': 'ja-JP',
        # Add more mappings as needed
    }
    return language_map.get(country_code, 'en-US')  # Default to English if not found

def main(ip):
    country_code = get_country_code(ip)
    if country_code:
        language = get_default_language(country_code)
        print(f'Default Accept-Language for IP {ip} (Country: {country_code}): {language}')
    else:
        print('Could not determine the country for the given IP.')

# Example usage
if __name__ == '__main__':
    user_ip = '8.8.8.8'  # Replace with the user's IP address
    main(user_ip)
