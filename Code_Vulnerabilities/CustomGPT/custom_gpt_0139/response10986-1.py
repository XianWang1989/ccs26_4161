
import requests

def get_country_code(ip_address):
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    if response.status_code == 200:
        data = response.json()
        return data.get("countryCode")
    return None

def get_default_accept_headers(country_code):
    # Mapping of country codes to default Accept-Language and Accept-Charset headers
    language_map = {
        'US': ('en-US,en;q=0.9', 'UTF-8'),
        'DE': ('de-DE,de;q=0.9', 'ISO-8859-1'),
        'FR': ('fr-FR,fr;q=0.9', 'UTF-8'),
        'RU': ('ru-RU,ru;q=0.9', 'windows-1251'),
        # Add more countries as necessary
    }

    return language_map.get(country_code, ('en-US,en;q=0.9', 'UTF-8'))  # default to English if not found

# Example usage
ip_address = "8.8.8.8"  # Example IP address
country_code = get_country_code(ip_address)
if country_code:
    accept_language, accept_charset = get_default_accept_headers(country_code)
    print(f"Default Accept-Language: {accept_language}")
    print(f"Default Accept-Charset: {accept_charset}")
else:
    print("Could not determine country code.")
