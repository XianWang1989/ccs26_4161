
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country')

# Mapping of country codes to default Accept-Language and Accept-Charset
language_charset_mapping = {
    'US': ('en-US', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    'CN': ('zh-CN', 'GB2312'),
    # Add more mappings as needed
}

# Function to get the default headers based on IP
def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in language_charset_mapping:
        return language_charset_mapping[country_code]
    else:
        # Default values if country is not found
        return ('en-US', 'UTF-8')

# Example usage
ip_address = '8.8.8.8'  # Replace with dynamic IP if necessary
default_language, default_charset = get_default_headers(ip_address)
print(f'Default Language: {default_language}, Default Charset: {default_charset}')
