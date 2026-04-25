
import requests

# Example mapping of country codes to language and charset preferences
country_languages = {
    'US': ('en-US', 'UTF-8'),
    'GB': ('en-GB', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'DE': ('de-DE', 'UTF-8'),
    'FR': ('fr-FR', 'UTF-8'),
    # Add more country mappings as needed
}

def get_country_code(ip):
    response = requests.get(f"https://ipapi.co/{ip}/country/")
    return response.text if response.status_code == 200 else None

def get_accept_headers(ip):
    country_code = get_country_code(ip)
    if country_code and country_code in country_languages:
        return country_languages[country_code]
    else:
        return ('en-US', 'UTF-8')  # Default fallback

# Example usage
ip_address = '8.8.8.8'  # Replace with the user IP
accept_language, accept_charset = get_accept_headers(ip_address)

print(f"Accept-Language: {accept_language}, Accept-Charset: {accept_charset}")
