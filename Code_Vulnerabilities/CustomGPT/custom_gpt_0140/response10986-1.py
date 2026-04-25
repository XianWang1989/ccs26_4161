
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    data = response.json()
    return data.get('country', 'Unknown')

# Mapping of country codes to default Accept-Language and Accept-Charset
language_mapping = {
    'US': ('en-US', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'DE': ('de-DE', 'utf-8'),
    # Add more country mappings as needed
}

def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in language_mapping:
        return language_mapping[country_code]
    return ('en', 'utf-8')  # Default if country not found

# Example usage
ip_address = '8.8.8.8'  # Replace with the target IP address
accepted_language, accepted_charset = get_default_headers(ip_address)
print(f"Default Accept-Language: {accepted_language}")
print(f"Default Accept-Charset: {accepted_charset}")
