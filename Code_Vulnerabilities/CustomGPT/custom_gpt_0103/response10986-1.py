
import requests

# Step 1: Get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get("country")

# Step 2: Map country codes to language and charset
language_charset_mapping = {
    'US': ('en-US', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    # Add more as needed
}

# Step 3: Determine the default headers based on country code
def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in language_charset_mapping:
        return {
            'Accept-Language': language_charset_mapping[country_code][0],
            'Accept-Charset': language_charset_mapping[country_code][1]
        }
    else:
        return {
            'Accept-Language': 'en-US',
            'Accept-Charset': 'UTF-8'  # Default fallback
        }

# Example usage
ip_address = '8.8.8.8'  # Replace with user's IP
default_headers = get_default_headers(ip_address)
print(default_headers)
