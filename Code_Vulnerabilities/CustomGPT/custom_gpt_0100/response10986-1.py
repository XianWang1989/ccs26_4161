
import requests

# Mapping of country codes to accept-language and accept-charset
country_language_map = {
    'US': ('en-US,en;q=0.5', 'UTF-8'),
    'RU': ('ru-RU,ru;q=0.9', 'windows-1251'),
    'FR': ('fr-FR,fr;q=0.8', 'UTF-8'),
    # Add more mappings as needed
}

def get_country_code(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    return data.get('country')

def default_accept_headers(ip):
    country_code = get_country_code(ip)
    if country_code in country_language_map:
        accept_language, accept_charset = country_language_map[country_code]
    else:
        accept_language, accept_charset = ('en-US', 'UTF-8')  # Default headers

    return {
        'Accept-Language': accept_language,
        'Accept-Charset': accept_charset
    }

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
headers = default_accept_headers(ip_address)
print(headers)
