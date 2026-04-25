
import requests

# Example mapping of country codes to commonly used Accept-Language and Accept-Charset
country_language_mapping = {
    'US': {'language': 'en-US', 'charset': 'UTF-8'},
    'RU': {'language': 'ru-RU', 'charset': 'windows-1251'},
    'FR': {'language': 'fr-FR', 'charset': 'UTF-8'},
    'CN': {'language': 'zh-CN', 'charset': 'UTF-8'},
    # Add more mappings as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    return data.get('country')  # Returns country code

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code in country_language_mapping:
        return country_language_mapping[country_code]
    return {'language': 'en', 'charset': 'UTF-8'}  # Fallback option

# Example usage
ip_address = '8.8.8.8'  # Replace with the desired IP
headers = get_default_headers(ip_address)

print(f"Default Accept-Language: {headers['language']}")
print(f"Default Accept-Charset: {headers['charset']}")
