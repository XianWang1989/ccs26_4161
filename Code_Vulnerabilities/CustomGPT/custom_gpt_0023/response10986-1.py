
import ipinfo

# Your IPinfo token here
ACCESS_TOKEN = 'YOUR_IPINFO_ACCESS_TOKEN'
handler = ipinfo.getHandler(ACCESS_TOKEN)

# Mapping of country codes to Accept-Language and Accept-Charset
country_languages = {
    'US': ('en-US,en;q=0.5', 'utf-8'),
    'RU': ('ru-RU,ru;q=0.9', 'windows-1251'),
    'FR': ('fr-FR,fr;q=0.9', 'utf-8'),
    'DE': ('de-DE,de;q=0.9', 'utf-8'),
    # Add more countries as needed
}

def get_default_headers(ip_address):
    details = handler.getDetails(ip_address)
    country_code = details['country']

    # Get default headers based on the country code
    headers = country_languages.get(country_code, ('en;q=0.9', 'utf-8'))

    return headers

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP address
accept_language, accept_charset = get_default_headers(ip)
print(f"Accept-Language: {accept_language}")
print(f"Accept-Charset: {accept_charset}")
