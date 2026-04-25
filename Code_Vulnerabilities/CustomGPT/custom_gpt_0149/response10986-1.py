
import requests

def get_country_from_ip(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    return data.get('country'), data.get('country_name')

def get_default_language_and_charset(country_code):
    # Define default languages and charsets for specific countries
    language_map = {
        'US': ('en-US', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'DE': ('de-DE', 'ISO-8859-1'),
        # Add more countries as needed
    }
    return language_map.get(country_code, ('en', 'UTF-8'))  # Default to English if country is not found

def main(ip_address):
    country_code, country_name = get_country_from_ip(ip_address)
    if country_code:
        language, charset = get_default_language_and_charset(country_code)
        print(f"Country: {country_name} ({country_code})")
        print(f"Default Accept-Language: {language}")
        print(f"Default Accept-Charset: {charset}")
    else:
        print("Could not determine country from IP address.")

# Example usage
ip = "8.8.8.8"  # Replace with the user's IP address
main(ip)
