
import requests

def get_country_code(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()

    return data.get("country")

def default_headers(ip_address):
    country_code = get_country_code(ip_address)

    # Define common languages and charsets by country code
    lang_charset = {
        'US': ('en-US', 'utf-8'),
        'GB': ('en-GB', 'utf-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'DE': ('de-DE', 'utf-8'),
        'FR': ('fr-FR', 'utf-8'),
        'ES': ('es-ES', 'utf-8'),
        # Add more countries as needed
    }

    # Get headers based on country code or default to utf-8
    lang, charset = lang_charset.get(country_code, ('en-US', 'utf-8'))

    return {
        'Accept-Language': lang,
        'Accept-Charset': charset
    }

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
headers = default_headers(ip_address)
print(headers)
