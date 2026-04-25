
import requests

# A mapping of country codes to their most common Accept-Language and Accept-Charset headers
country_language_map = {
    'US': ('en-US,en;q=0.9', 'UTF-8'),
    'FR': ('fr-FR,fr;q=0.9', 'UTF-8'),
    'DE': ('de-DE,de;q=0.9', 'UTF-8'),
    'RU': ('ru-RU,ru;q=0.9', 'windows-1251'),
    'CN': ('zh-CN,zh;q=0.9', 'UTF-8'),
    # Add more country mappings as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')

    if response.status_code == 200:
        data = response.json()
        return data.get('country', None)  # Return country code
    return None

def determine_accept_headers(ip_address):
    country_code = get_country_code(ip_address)

    if country_code:
        return country_language_map.get(country_code, ('en-US,en;q=0.9', 'UTF-8'))  # Default to US if not found
    return ('en-US,en;q=0.9', 'UTF-8')  # Fallback default

# Example usage
ip = '8.8.8.8'  # Example IP address
accept_language, accept_charset = determine_accept_headers(ip)
print(f'Accept-Language: {accept_language}, Accept-Charset: {accept_charset}')
