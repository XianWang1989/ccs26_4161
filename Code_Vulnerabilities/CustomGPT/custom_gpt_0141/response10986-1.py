
import requests

# Mapping of country codes to default Accept-Language and Accept-Charset
country_language_map = {
    'US': ('en-US', 'utf-8'),
    'FR': ('fr-FR', 'utf-8'),
    'DE': ('de-DE', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),  # Common for Russian users
    'CN': ('zh-CN', 'utf-8'),          # Common for Chinese users
    # Add more mappings as needed
}

def get_country_code(ip_address):
    # Use an IP geolocation service to determine the country code
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = response.json()
    country_code = data.get('country', 'US')  # Default to US if not found
    return country_code

def get_default_accept_headers(ip_address):
    country_code = get_country_code(ip_address)
    accept_language, accept_charset = country_language_map.get(country_code, ('en-US', 'utf-8'))
    return accept_language, accept_charset

# Example usage
if __name__ == "__main__":
    user_ip = '8.8.8.8'  # Replace with the user's IP address
    accept_language, accept_charset = get_default_accept_headers(user_ip)
    print(f'Default Accept-Language: {accept_language}')
    print(f'Default Accept-Charset: {accept_charset}')
