
import requests

# Function to get country code from IP address
def get_country_code(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()
    return data.get('country', '')  # Returns the country code

# Mapping of country codes to Accept-Language and Accept-Charset
country_language_mapping = {
    'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'utf-8'},
    'GB': {'Accept-Language': 'en-GB,en;q=0.9', 'Accept-Charset': 'utf-8'},
    'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251'},
    'FR': {'Accept-Language': 'fr-FR,fr;q=0.9', 'Accept-Charset': 'utf-8'},
    # Add more mappings as needed
}

# Function to determine the default headers based on IP
def determine_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    headers = country_language_mapping.get(country_code, {'Accept-Language': 'en', 'Accept-Charset': 'utf-8'})
    return headers

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
default_headers = determine_default_headers(ip_address)
print(f"Default Headers for {ip_address}: {default_headers}")
