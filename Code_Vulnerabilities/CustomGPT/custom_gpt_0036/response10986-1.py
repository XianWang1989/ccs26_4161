
import requests

# Step 1: Function to get country code from IP address
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country', None)

# Step 2: Create a mapping of country codes to default Accept-Language and Accept-Charset
country_language_map = {
    'US': ('en-US', 'UTF-8'),
    'GB': ('en-GB', 'UTF-8'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    # Add more country codes and their defaults as needed
}

# Step 3: Function to get the default Accept-Language and Accept-Charset based on IP
def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in country_language_map:
        return country_language_map[country_code]
    else:
        # Return a default value if the country is unknown
        return ('en-US', 'UTF-8')  # Fallback to English and UTF-8

# Example usage
user_ip = '8.8.8.8'  # Replace with actual user IP
language, charset = get_default_headers(user_ip)

print(f'Default Accept-Language: {language}, Accept-Charset: {charset}')
