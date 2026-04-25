
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data.get('country')

# Function to map country code to default Accept-Language and Accept-Charset
def get_default_headers(country_code):
    # Example mapping; extend these as necessary
    language_map = {
        'US': ('en-US', 'utf-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'DE': ('de-DE', 'utf-8'),
        'FR': ('fr-FR', 'utf-8'),
        # Add more country mappings as needed
    }
    return language_map.get(country_code, ('en', 'utf-8'))  # Default to English

# Example usage
ip_address = '8.8.8.8'  # Replace this with the user's IP
country_code = get_country_code(ip_address)

# Get default Accept-Language and Accept-Charset
language, charset = get_default_headers(country_code)

print(f"Country Code: {country_code}, Accept-Language: {language}, Accept-Charset: {charset}")
