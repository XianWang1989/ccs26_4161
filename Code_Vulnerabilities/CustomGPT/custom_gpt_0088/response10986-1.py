
import requests

# Sample mapping of country codes to Accept-Language and Accept-Charset
country_language_mapping = {
    'US': ('en-US,en;q=0.5', 'utf-8'),
    'RU': ('ru-RU,ru;q=0.9', 'windows-1251'),
    'FR': ('fr-FR,fr;q=0.9', 'utf-8'),
    'DE': ('de-DE,de;q=0.9', 'utf-8'),
    # Add more country mappings as needed
}

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/country/')
    return response.text.strip()

def get_default_headers(ip):
    country_code = get_country_code(ip)
    headers = country_language_mapping.get(country_code, ('en-US,en;q=0.5', 'utf-8'))
    return headers

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
language, charset = get_default_headers(ip_address)
print(f"Default Accept-Language: {language}")
print(f"Default Accept-Charset: {charset}")
