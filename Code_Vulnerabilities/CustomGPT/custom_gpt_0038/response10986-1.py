
import requests

# Mapping of country codes to default Accept-Language and Accept-Charset headers
country_languages = {
    'US': {'language': 'en-US', 'charset': 'utf-8'},
    'RU': {'language': 'ru-RU', 'charset': 'windows-1251'},
    'FR': {'language': 'fr-FR', 'charset': 'utf-8'},
    # Add more country codes as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=YOUR_API_KEY&ip={ip_address}')
    data = response.json()
    return data.get('country_code2')  # 2-letter country code

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)

    if country_code in country_languages:
        return country_languages[country_code]
    else:
        return {'language': 'en', 'charset': 'utf-8'}  # Default headers for unknown country

# Example usage
ip = '8.8.8.8'  # Replace with the actual IP address
default_headers = get_default_headers(ip)
print(f"Default Accept-Language: {default_headers['language']}, Accept-Charset: {default_headers['charset']}")
