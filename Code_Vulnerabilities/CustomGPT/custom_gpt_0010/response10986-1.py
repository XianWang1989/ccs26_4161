
import requests

# Sample mapping of country codes to Accept-Language and Charset
country_language_map = {
    'US': ('en-US', 'UTF-8'),
    'ES': ('es-ES', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    # Add more country mappings as needed
}

def get_country_code(ip_address):
    try:
        response = requests.get(f"https://ipapi.co/{ip_address}/json/")
        data = response.json()
        return data.get('country')
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return None

def get_default_accept_language(ip_address):
    country_code = get_country_code(ip_address)
    if country_code and country_code in country_language_map:
        lang, charset = country_language_map[country_code]
        return lang, charset
    else:
        return None, None

# Example usage
ip = '8.8.8.8'  # Replace with the actual IP address
language, charset = get_default_accept_language(ip)

if language and charset:
    print(f"Default Accept-Language: {language}, Accept-Charset: {charset}")
else:
    print("No mapping found for the IP address.")

