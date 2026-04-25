
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country', None)

# Mapping of country codes to default Accept-Language and Accept-Charset headers
country_lang_mapping = {
    'US': {'Accept-Language': 'en-US', 'Accept-Charset': 'UTF-8'},
    'RU': {'Accept-Language': 'ru-RU', 'Accept-Charset': 'windows-1251'},
    'DE': {'Accept-Language': 'de-DE', 'Accept-Charset': 'ISO-8859-1'},
    # Add more country mappings as needed
}

# Function to get default headers based on IP
def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in country_lang_mapping:
        return country_lang_mapping[country_code]
    else:
        # Return some default headers if country is unknown
        return {'Accept-Language': 'en', 'Accept-Charset': 'UTF-8'}

# Example usage
ip_address = '8.8.8.8'  # Replace with the IP address you want to check
headers = get_default_headers(ip_address)
print(headers)
