
import requests

# Example mapping of country codes to languages and charsets
country_language_map = {
    'US': ('en-US', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    'CN': ('zh-CN', 'GB2312'),
    # Add more mappings as needed
}

def get_country_code(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data.get('country')

def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in country_language_map:
        return country_language_map[country_code]
    else:
        return ('en', 'UTF-8')  # Default values

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
accept_language, accept_charset = get_default_headers(ip_address)

print(f"Default Accept-Language: {accept_language}")
print(f"Default Accept-Charset: {accept_charset}")
