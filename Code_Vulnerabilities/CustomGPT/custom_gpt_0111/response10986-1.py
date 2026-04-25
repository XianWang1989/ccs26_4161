
import geocoder

# Mapping of country codes to default Accept-Language and Accept-Charset
lang_charset_mapping = {
    'US': ('en-US', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'iso-8859-1'),
    'DE': ('de-DE', 'utf-8'),
    # Add more countries as needed
}

def get_default_accept_headers(ip_address):
    # Get the country code using the geocoder library
    g = geocoder.ip(ip_address)

    if g.ok and g.country:
        country_code = g.country
        # Look up the language and charset based on country code
        language, charset = lang_charset_mapping.get(country_code, ('en-US', 'utf-8'))  # Default to en-US if not found
        return {
            'Accept-Language': language,
            'Accept-Charset': charset
        }
    else:
        # Handle cases where geolocation fails
        return {
            'Accept-Language': 'en-US',
            'Accept-Charset': 'utf-8'
        }

# Example usage
ip = '8.8.8.8'  # Replace with the user's IP address
headers = get_default_accept_headers(ip)
print(headers)
